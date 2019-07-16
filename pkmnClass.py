#Pokemon class

#Other modifications
#add weather effects
#add stat change probabilities
#add damage variations (multi hits, low kick based on weight, seismic toss based on level)
#include catch rate probability?




#-----------------------------------------------modify to find type/s given just the name (need database)
class Pokemon:
    type1 = ""
    type2 = ""

    #may consider adding Nature effects later -- a bit complex
    nature = ""

    #max out moveCount at 4
    moveCount = 0
    
    #dictionary of moves and its attributes
    moves_dict = {}

    #dictionary of base stats with minimum default values
    baseStats_dict = {"Level":5,"HP":1,"ATK":0,"DEF":1,"SP.ATK":0,"SP.DEF":1,"SPD":1}

    #list of statuses: burn, frozen, paralyzed, poison, badly poisoned, sleep, fainted, confused, infatuated
    status_list = ["","BRN","FRZ","PAR","PSN","BPSN","SLP","FNT","CNF","IFT"]

    #valid types
    types_dict = {"normal":{"rock":0.5, "ghost":0, "steel":0.5},\
                        "fighting":{"normal":2, "flying":0.5, "poison":0.5,"rock":2,"bug":0.5,"ghost":0,"steel":2,"psychic":0.5,"ice":2,"dark":2,"fairy":0.5},\
                        "flying":{"fighting":2, "rock":0.5, "bug":2,"steel":0.5, "grass":2, "electric":0.5},\
                        "poison":{"poison":0.5,"ground":0.5, "rock":0.5, "ghost":0.5,"steel":0,"grass":2,"fairy":2},\
                        "ground":{"flying":0, "poison":2,"rock":2,"bug":0.5,"steel":2,"fire":2,"grass":0.5,"electric":2},\
                        "rock":{"fighting":0.5,"flying":2,"ground":0.5,"bug":2,"steel":0.5,"fire":2,"ice":2},\
                        "bug":{"fighting":0.5,"flying":0.5,"poison":0.5,"ghost":0.5,"steel":0.5,"fire":0.5,"grass":2,"psychic":2,"dark":2,"fairy":0.5},\
                        "ghost":{"normal":0,"ghost":2,"psychic":2,"dark":0.5},\
                        "steel":{"rock":2,"steel":0.5,"fire":0.5,"water":0.5,"electric":0.5,"ice":2,"fairy":2},\
                        "fire":{"rock":0.5,"bug":2,"steel":2,"fire":0.5,"water":0.5,"grass":2,"ice":2,"dragon":0.5},\
                        "water":{"ground":2,"rock":2,"fire":2,"water":0.5,"grass":0.5,"dragon":0.5},\
                        "grass":{"flying":0.5,"poison":0.5,"ground":2,"rock":2,"bug":0.5,"steel":0.5,"fire":0.5,"water":2,"grass":0.5,"dragon":0.5},\
                        "electric":{"flying":2,"ground":0,"water":2,"grass":0.5,"electric":0.5,"dragon":0.5},\
                        "psychic":{"fighting":2,"poison":2,"steel":0.5,"psychic":0.5,"dark":0},\
                        "ice":{"flying":2,"ground":2,"steel":0.5,"fire":0.5,"water":0.5,"grass":2,"ice":0.5,"dragon":2},\
                        "dragon":{"steel":0.5,"dragon":2,"fairy":0},\
                        "dark":{"fighting":0.5,"ghost":2,"psychic":2,"dark":0.5,"fairy":0.5},\
                        "fairy":{"fighting":2,"poison":0.5,"steel":0.5,"fire":0.5,"dragon":2,"dark":2}}
    
    def __init__(self,name,type1,type2 = ""):
        self.name = name
        if isValidType(type1,self.types_dict):
            self.type1 = type1
        if type2 == "" or isValidType(type2,self.types_dict):
            self.type2 = type2

    def __str__(self): #creates a string representation of itself
        identity = "Pokemon"
        moves = "Moveset:"
        if self.type2 == "":
            identity = self.name+" is a "+self.type1+"-type Pokemon."
        else:
            identity = self.name+" is a "+self.type1+"-"+self.type2+" dual-type Pokemon."

        for move in self.moves_dict:
            moves += "\n"+move.title()
        return identity +"\n"+moves

    #----------------------------------------------------------considers all strategies and chooses best one according to damage output
    #def findBestMove(self, dmg, acc):

##    #same type attack bonus
##    def STAB(self, moveType):
##        stabValid = False
##        if self.type1 or self.type2 == moveType:
##            stabValid = True
##        return stabValid

    #checks if move is in movelist
    def checkMove(self,moveName):
        valid = False
        if moveName.lower() in self.moves_dict:
            valid = True
        return valid
    
    #setMove - moveName, moveType, effect (physical, special), raw damage (w/o considering other conditions), accuracy, power points

    def setMove(self,moveName,moveType,effect,rawDmg,acc, pp):
        #local var: move_attributes
        move_attributes = []
        if self.moveCount < 4:
            if effect.lower() == "special":
                rawDmg = 0
            move_attributes += [moveType,effect,rawDmg,acc,pp]
            self.moves_dict[moveName.lower()] = move_attributes
            self.moveCount += 1
        else:
            ans = input(self.name+" currently has four moves. Would you like to replace a move? Yes|No\n")
            if ans.lower() == "no":
                pass
            elif ans.lower() == "yes":                
                for move in self.moves_dict:
                    print(move.title())
                move2Replace = input()
                self.replaceMove(move2Replace,moveName,moveType,effect,rawDmg,acc,pp)
            else:
                print("Please enter a valid answer.")

    #replaces a move
    def replaceMove(self,move2Repl,moveName,moveType,effect,rawDmg,acc,pp):
        self.delMove(move2Repl)
        self.moves_dict[moveName] = [moveType,effect,rawDmg,acc,pp]
        
    #deletes known move
    def delMove(self,moveName):
        if self.checkMove(moveName):
            del self.moves_dict[moveName]
        else:
            print(self.name +" doesn't know the move "+ moveName +"!")

    #gets move attributes info
    def getMoveAttr(self,moveName):
        if self.checkMove(moveName):
            moveType = self.moves_dict[moveName][0]
            effect = self.moves_dict[moveName][1]
            damage = str(self.moves_dict[moveName][2])
            accuracy = str(self.moves_dict[moveName][3])
            powerPoints = str(self.moves_dict[moveName][4])

            return moveType,effect,damage,accuracy,powerPoints

    #prints move attributes
    def printMoveAttr(self,moveName):
        if self.checkMove(moveName):
            moveType,effect,damage,accuracy,pp = self.getMoveAttr(moveName)
            print("-----"+moveName.title()+"-----\nType: "+moveType+\
                  "\nEffect: "+effect+\
                  "\nDamage: "+damage+\
                  "\nAccuracy: "+accuracy+\
                  "\nPP:"+pp)
            
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
    def setStats2(self, lvl,hp,atk,dfn,sp_atk,sp_def,spd):
        self.baseStats_dict["Level"] = lvl
        self.baseStats_dict["HP"] = hp
        self.baseStats_dict["ATK"] = atk
        self.baseStats_dict["DEF"] = dfn
        self.baseStats_dict["SP.ATK"] = sp_atk
        self.baseStats_dict["SP.DEF"] = sp_def
        self.baseStats_dict["SPD"] = spd

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
        lvl = self.baseStats_dict["Level"]
        HP = self.baseStats_dict["HP"]
        attack = self.baseStats_dict["ATK"]
        defense = self.baseStats_dict["DEF"]
        sp_attack = self.baseStats_dict["SP.ATK"]
        sp_defense = self.baseStats_dict["SP.DEF"]
        speed = self.baseStats_dict["SPD"]
        return lvl, HP, attack, defense, sp_attack, sp_defense, speed

    #prints stats
    def printStats(self):
        lvl, hp, att, defense, spAtt,spDef, spd = self.getStats()
        print("Level:",lvl,\
              "\nHP:",hp,\
              "\nATK:",att,\
              "\nDEF:",defense,\
              "\nSP.ATK:",spAtt,\
              "\nSP.DEF:",spDef,\
              "\nSPD:",spd)


    #prints attributes a specific move
##    def printMoveAttr(self,moveName):
##        if self.checkMove(moveName):
##
##            print("-----"+moveName.title()+"-----\nType: "+self.moves_dict[moveName][0]+\
##                  "\nEffect: "+self.moves_dict[moveName][1]+\
##                  "\nDamage: "+str(self.moves_dict[moveName][2])+\
##                  "\nAccuracy: "+str(self.moves_dict[moveName][3]))

#checks if valid type
def isValidType(type1,types_dict):
        valid = False
        try:
            type1 = type1.lower()
            if type1 in types_dict:
                valid = True      
        except:
            raise ValueError
        else:
            if type1 not in types_dict:
                print("Please enter valid types from this list:\n")
                for key in types_dict:
                    print(key)
                #main() ------------------------------------------add main() later
            else:
                pass
        return valid

    
Char = Pokemon("Charmander","fire")
Char.setMove("Growl","normal","special",0,100,30)
Char.setMove("Scratch","normal","physical",10,100,45)
Char.setMove("Smokescreen","normal","special",0,100,25)
Char.setMove("Ember","fire","physical",30,100,35)
#Char.setMove("Flamethrower","fire","physical",80,100,25)
#Char.printMoveAttr("growl")
Char.setStats2(5,30,10,10,10,10,15)
Char.influenceStat("HP",-15)
Kip = Pokemon("Mudkip","water","ground")

