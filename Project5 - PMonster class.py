#Pokemon Battle Sim


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

    #list of move attributes: moveName, moveType, effect (physical, special), raw damage (w/o considering other conditions), accuracy
    #-----------------------------------------------------------add Power points later?
##    move1_attributes = []
##    move2_attributes = []
##    move3_attributes = []
##    move4_attributes = []

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
    
    #move1 - moveName, moveType, effect (physical, special), raw damage (w/o considering other conditions), accuracy
    def setMove(self,moveName,moveType,effect,rawDmg,acc):
        #local var: move_attributes
        move_attributes = []
        if self.moveCount < 4:
            if effect.lower() == "special":
                rawDmg = 0
            move_attributes += [moveType,effect,rawDmg,acc]
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
                self.replaceMove(move2Replace,moveName,moveType,effect,rawDmg,acc)
            else:
                print("Please enter a valid answer.")
            

    def replaceMove(self,move2Repl,moveName,moveType,effect,rawDmg,acc):
        self.delMove(move2Repl)
        self.moves_dict[moveName] = [moveType,effect,rawDmg,acc]
        
    #deletes known move
    def delMove(self,moveName):
        if moveName.lower() in self.moves_dict:
            del self.moves_dict[moveName]
        else:
            print(self.name +" doesn't know the move "+ moveName +"!")

##    def getMove(self,moveName):

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
Char.setMove("Growl","normal","special",0,100)
Char.setMove("Scratch","normal","physical",10,100)
Char.setMove("Smokescreen","normal","special",0,100)
Char.setMove("Ember","fire","physical",30,100)
#Char.setMove("Flamethrower","fire","physical",80,100)
Kip = Pokemon("Mudkip","water","ground")

