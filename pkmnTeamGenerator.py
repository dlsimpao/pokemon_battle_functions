#Pokemon party generator
#possible additions
#1. Optimized Pokemon party gen
#2. Guided Pokemon party creator, given initial user choices, recommends next choice
#3. Themed Party gen



#working
#1. creating random moves for each pokemon object
#2. set moves, get moves
#Solutions


import conventionalCode as cc
import pkmnData as pd
import PMonsterClass as pmc
import random

class pkmnTeam():
    #dictionary with names as keys and objects as values
    pkmn_dict = {}
    pkmn_fieldStatus = ["In Battle","FNT"]

    def __init__(self, pkmn_list = []):

        self.setParty(pkmn_list)
        self.partyCount = len(pkmn_list)



    def addMember(self, pkmnToAdd):
        pkmnToAdd = pkmnToAdd.title()
        if self.isValidName(pkmnToAdd):
            if self.partyCount < 6:
                #uses Pokemon class and adds to the class team
                obj = pmc.Pokemon(pkmnToAdd)
                self.pkmn_dict[pkmnToAdd] = obj
                self.partyCount += 1
            else:
                #self.printParty()
                pkmnToSwap = input("Your party is full. Please select a Pokemon to swap.\n")
                pkmnToSwap = pkmnToSwap.title()
                if (pkmnToSwap in self.pkmn_dict) or (pkmnToSwap == pkmnToAdd):
                    self.swapMember(pkmnToAdd,pkmnToSwap)
                else:
                    print(pkmnToSwap+" is not found.")
                    self.addMember(pkmnToAdd)
        else:
            print("The Pokedex does not recognize this name.")

    def swapMember(self, pkmnIn, pkmnOut):
        if pkmnIn != pkmnOut:
            for mon in self.pkmn_dict:
                if mon == pkmnOut:
                    self.pkmn_dict.pop(mon)
                    break
            self.partyCount -= 1
            self.addMember(pkmnIn)
        else:
            print(pkmnIn.title()+" will not be added.")
        
        
    def isValidName(self, name, nameCategory = "Pokemon"):
        nameCategory = nameCategory.title()
        valid = False
        try:
            fHandle = pd.getFHandle(nameCategory)
        except:
            raise(NameError)
        pkmnNames = pd.autoDict(fHandle,index = False)
        if name in pkmnNames:
            valid = True
        return valid


#Modify to get types from pokemon
    def randomizeMoves(self,pkmnName):
        for mon in self.pkmn_dict:
            if mon == pkmnName:
                self.pkmn_dict[mon].setMove(genPokeMoves(4,["Dragon"]))
                break

    def getMoves(self,pkmnName):
        retList = []
        for mon in self.pkmn_list:
            if mon == pkmnName:
                retList = mon.getMoves()
                break
        return retList
                
            
    def randomizeParty(self,num):
        self.setParty(genPokeTeam(num))

    def setParty(self,party_list):
        self.pkmn_list = []
        notRec = []
        if len(party_list) <= 6:
            for mon in party_list:
                if isValidName(mon, "Pokemon"):
                    mon = mon.title()
                    self.addMember(mon)
                else:
                    notRec.append(mon)
            if notRec != []:
                print("The Pokedex does not recognize the name/s: "+str(notRec))       
        else:
            print("You can only set a party of max 6 Pokemon")

    def getParty(self):
        return self.pkmn_dict

    def printParty(self):
        party = self.getParty()
        for mon in party:
            print(mon)

            
#-------------------------------------------------------------------------------------
#add restrictions like type, gen
def genPokeTeam(num):
    pokeTeam_list = []
    pokeName_dict = {}

    fHandle = pd.getFHandle("Pokemon")
    #fHandle.readline()
    pokeName_dict = pd.autoDict(fHandle,["Pokemon"])

    while len(pokeTeam_list) != num:
        ranVal = random.randint(1,len(pokeName_dict))
        pokeTeam_list.append(pokeName_dict[ranVal])
    return pokeTeam_list


#function takes in number of pokeMoves, type and type category restrictions
def genPokeMoves(num,typeList = [], cat = []):
    pokeMoves = []
    filtMoves_dict = {} #for type-specific moves
    
    fHandle = pd.getFHandle("Moves")
    pokeMoves_dict = pd.autoDict(fHandle,["Name","Type","Cat."],index = True)
    f = 1#new index for filtered dictionary
    
    #fills in the filtered dictionary based on restrictions given
    if typeList != [] and cat != []: #if type and category restrictions apply
        typeList = [x.title() for x in typeList]
        for i in pokeMoves_dict:
            #print(pokeMoves_dict[move][1].title())
            if pokeMoves_dict[i][1].title() in typeList\
               and pokeMoves_dict[i][2].title() in cat:
                filtMoves_dict[f] = pokeMoves_dict[i][0]
                f += 1
        pokeMoves = createRandList(num, filtMoves_dict, unique = True)
    elif typeList != [] and cat == []: #if type restrictions apply
        typeList = [x.title() for x in typeList]
        for i in pokeMoves_dict:
            #print(pokeMoves_dict[move][1].title())
            if pokeMoves_dict[i][1].title() in typeList:
                filtMoves_dict[f] = pokeMoves_dict[i][0]
                f += 1
        pokeMoves = createRandList(num, filtMoves_dict, unique = True)

    elif typeList == [] and cat == []: #if category restrictions apply
        typeList = [x.title() for x in typeList]
        for i in pokeMoves_dict:
            #print(pokeMoves_dict[move][1].title())
            if pokeMoves_dict[i][2].title() in cat:
                filtMoves_dict[f] = pokeMoves_dict[i][0]
                f += 1
        pokeMoves = createRandList(num, filtMoves_dict, unique = True)
    else:
        pokeMoves = createRandList(num, pokeMoves_dict, unique = True)

    return pokeMoves

#genPokeMoves helper
#creates a random unique list of size num from a dictionary with integers as its keys
def createRandList(num, d, unique = True):
    l = []
    try:
        while len(l) != num:
            ranVal = random.randint(1,len(d))
            if unique:
                if d[ranVal] not in l:
                    l.append(d[ranVal])
            else:
                l.append(d[ranVal])
    except:
        raise(ValueError)
    return l


        

##moveList = genPokeMoves(4,["Electric"])
##print(moveList)


##alist = genPokeTeam(6)
##print(alist)
pkmn_list = ["Heatran","Gallade","Zigzagoon","Entei","Espeon","Rattata"]
Red = pkmnTeam()
#Red.randomizeParty(6)  
for pkmn in pkmn_list:
    Red.addMember(pkmn)
Red.printParty()
cc.space(3)
##Red.addMember("charizard")
Red.randomizeMoves("Zigzagoon")


