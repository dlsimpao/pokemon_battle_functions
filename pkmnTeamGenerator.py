#Pokemon party generator
#possible additions
#1. Optimized Pokemon party gen
#2. Guided Pokemon party creator
#3. Themed Party gen


#Solutions


import conventionalCode as cc
import pkmnData as pd
import PMonsterClass as pmc
import random

class pkmnTeam():
    def __init__(self, pkmn_list):
        self.pkmn_list = pkmn_list
        self.partyCount = len(pkmn_list)

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

    #fills in the filtered dictionary based on restrictions given
    if typeList != [] and cat != []: #if type and category restrictions apply
        typeList = [x.title() for x in typeList]
        f = 1#new index for filtered dictionary
        for i in pokeMoves_dict:
            #print(pokeMoves_dict[move][1].title())
            if pokeMoves_dict[i][1].title() in typeList\
               and pokeMoves_dict[i][2].title() in cat:
                filtMoves_dict[f] = pokeMoves_dict[i][0]
                f += 1
        pokeMoves = createRandList(num, filtMoves_dict, unique = True)
    elif typeList != [] and cat == []: #if type restrictions apply
        typeList = [x.title() for x in typeList]
        f = 1#new index for filtered dictionary
        for i in pokeMoves_dict:
            #print(pokeMoves_dict[move][1].title())
            if pokeMoves_dict[i][1].title() in typeList:
                filtMoves_dict[f] = pokeMoves_dict[i][0]
                f += 1
        pokeMoves = createRandList(num, filtMoves_dict, unique = True)

    elif typeList == [] and cat == []: #if category restrictions apply
        typeList = [x.title() for x in typeList]
        f = 1#new index for filtered dictionary
        for i in pokeMoves_dict:
            #print(pokeMoves_dict[move][1].title())
            if pokeMoves_dict[i][2].title() in cat:
                filtMoves_dict[f] = pokeMoves_dict[i][0]
                f += 1
        pokeMoves = createRandList(num, filtMoves_dict, unique = True)
    else:
        pokeMoves = createRandList(num, pokeMoves_dict, unique = True)

    return pokeMoves

#helps genPokeMoves()
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

