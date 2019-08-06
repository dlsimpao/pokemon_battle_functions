#Pokemon class

#Other modifications
#add weather effects
#add stat change probabilities
#add damage variations (multi hits, low kick based on weight, seismic toss based on level)
#include catch rate probability?

#methods - none

import pkmnData as pd
import conventionalCode as cc

class Pokemon:
    type1 = ""
    type2 = ""

    #may consider adding Nature effects later -- a bit complex, not used yet
    nature = ""

    #max out moveCount at 4
    moveCount = 0

    #list of statuses: burn, frozen, paralyzed, poison, badly poisoned, sleep, fainted, confused, infatuated
    status_list = ["Healthy","BRN","FRZ","PAR","PSN","BPSN","SLP","FNT","CNF","IFT"]

    #gets valid names and types from Pokemon data
    fHandle = pd.getFHandle("Pokemon")
    pkmnTypes_dict = pd.autoDict(fHandle,index = False)

    #gets valid moves
    fHandle2 = pd.getFHandle("Moves")
    moveAttrLabels = ["Name","Type","Cat.","Power","Acc.","PP"]
    pkmnMoves_dict = pd.autoDict(fHandle2,moveAttrLabels,index = False)
    
    def __init__(self,name):
        try:
            self.name = name
            self.type1, self.type2 = [*self.pkmnTypes_dict[name]]
        except:
            print("Please enter a valid Pokemon name")
        else:
            self.move_dict = {}
            self.status = "Healthy"
            self.baseStats_dict = {"Level":5,"HP":1,"ATK":0,"DEF":1,"SP.ATK":0,"SP.DEF":1,"SPD":1}
            
    def __str__(self): #creates a string representation of itself
        identity = "Pokemon"
        moves = "Moveset:"
        if self.type2 == "":
            identity = self.name+" is a "+self.type1+"-type Pokemon."
        else:
            identity = self.name+" is a "+self.type1+"-"+self.type2+" dual-type Pokemon."

        for move in self.move_dict:
            moves += "\n"+move.title()
        return identity +"\n"+ moves

    def getName(self):
        return self.name

    def getTypes(self):
        return [self.type1, self.type2]

    #checks if move is in movelist
    def checkMove(self,moveName):
        valid = False
        if moveName.lower() in self.move_dict:
            valid = True
        return valid
    
    def printMoveDict(self):
        for key in self.pkmnMoves_dict:
            print(key)

    def getMoves(self):
        retList = []
        for move in self.move_dict:
            retList.append(move)
        return retList

    def setMove(self,moveName):
        try:
            if self.moveCount < 4:
                self.move_dict[moveName] = self.pkmnMoves_dict[moveName]

                self.moveCount += 1
            else:
                for move in self.move_dict:
                    print(move)
                ans = input(self.name+" currently has four moves. Select a move to replace:n")
                if ans != moveName:
                    self.move_dict.pop(ans)
                    self.move_dict[moveName] = self.pkmnMoves_dict[moveName]
                else:
                    print(str(ans.title())+" will not be learned.")
        except:
            print("Please enter a valid move name.")

    #replaces a move
    def replaceMove(self,moveOut,moveIn):
        self.move_dict.pop(moveOut)
        self.move_dict[moveIn] = self.pkmnMoves_dict[moveIn]
        
    #deletes known move
    def delMove(self,moveName):
        if self.checkMove(moveName):
            del self.moves_dict[moveName]
        else:
            print(self.name +" doesn't know the move "+ moveName +"!")

    #returns move attribute dict
    def getMoveAttr(self,moveName):
        i = 1
        attr_dict = {}
        for moveAttr in self.pkmnMoves_dict[moveName]:
            attr_dict[self.moveAttrLabels[i]] = moveAttr
            i += 1
        return attr_dict

    #prints move attributes
    def printMoveAttr(self,moveName):
        attr_dict = self.getMoveAttr(moveName)
        print(moveName.title())
        for attr in attr_dict:
            print("{:<10}{:<20}".format(attr,attr_dict[attr]))
            
#  baseStats_dict = {"Level":5,"HP":1,"ATK":0,"DEF":1,"SP.ATK":0,"SP.DEF":1,"SPD":1}

    #sets stats (user friendly)
    def setStats(self):
        self.baseStats_dict["Level"] = input("Level: ")
        self.baseStats_dict["HP"] = input("HP: ")
        self.baseStats_dict["ATK"] = input("Attack: ")
        self.baseStats_dict["DEF"] = input("Defense: ")
        self.baseStats_dict["SP.ATK"] = input("Sp.Attack: ")
        self.baseStats_dict["SP.DEF"] = input("Sp.Defense: ")
        self.baseStats_dict["SPD"] = input("Speed: ")

    #sets stats
    def setStats2(self,lvl,hp,atk,dfn,sp_atk,sp_def,spd):
        self.baseStats_dict["Level"] = lvl
        self.baseStats_dict["HP"] = hp
        self.baseStats_dict["ATK"] = atk
        self.baseStats_dict["DEF"] = dfn
        self.baseStats_dict["SP.ATK"] = sp_atk
        self.baseStats_dict["SP.DEF"] = sp_def
        self.baseStats_dict["SPD"] = spd
        
    #may need to change later, but works fine logically
    #gameplay influencing stats, changes a specific stats by a certain amount
    #value > 0 for positive changes
    #value < 0 for negative changes
    def influenceStat(self,stat,value):
        change = self.baseStats_dict[stat] + value
        if stat in self.baseStats_dict:
            self.baseStats_dict[stat] = change
        else:
            print("Stat not recognized.")
        
    #returns stats
    def getStats(self):
        return self.baseStats_dict

    #prints stats
    def printStats(self):
        stats_dict = self.getStats()
        for stat in stats_dict:
            print("{:<10}{:<20}".format(stat,stats_dict[stat]))
   





Char = Pokemon("Charmander")
moveList = ["Growl","Scratch","Smokescreen","Ember"]

for move in moveList:
    Char.setMove(move)

#pd.printAllMoves(["Fire","electric","Rock","Dragon"])

##for move in pd.pkmnMoveType_dict:
##    print(pd.pkmnMoveType_dict[move])


##Char.printMoveAttr("growl")
##Char.setStats2(5,30,10,10,10,10,15)
##Char.influenceStat("HP",-15)
##Kip = Pokemon("Swampert")
##Kip.setMove("Water Gun")
##Kip.printMoveAttr("Water Gun")

