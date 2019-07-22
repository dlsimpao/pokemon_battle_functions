#Pokemon party generator
#possible additions
#1. Optimized Pokemon party gen
#2. Guided Pokemon party creator
#3. Themed Party gen

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


def genPokeMoves(num,typeList = []):
    pokeMoves = []
    filtMoves_dict = {} #for type-specific moves
    
    fHandle = pd.getFHandle("Moves")
    pokeMoves_dict = pd.autoDict(fHandle,["Name","Type"],index = True)

    #type-specific move setting
    if typeList != []:
        typeList = [x.title() for x in typeList]
        f = 1#new index for filtered dictionary
        for i in pokeMoves_dict:
            #print(pokeMoves_dict[move][1].title())
            if pokeMoves_dict[i][1].title() in typeList:
                filtMoves_dict[f] = pokeMoves_dict[i][0]
                f += 1
        while len(pokeMoves) != num:
            ranVal = random.randint(1,len(filtMoves_dict))
            if filtMoves_dict[ranVal] not in pokeMoves:
                pokeMoves.append(filtMoves_dict[ranVal])
    else:     
        while len(pokeMoves) != num:
            ranVal = random.randint(1,len(pokeMoves_dict))
            if pokeMoves_dict[ranVal] not in pokeMoves:
                pokeMoves.append(pokeMoves_dict[ranVal][0])
    return pokeMoves
        

##moveList = genPokeMoves(4,["Electric"])
##print(moveList)


##alist = genPokeTeam(6)
##print(alist)

