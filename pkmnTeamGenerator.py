#Pokemon party evaluator
#evaluates the party based 

import random
import PMonsterClass as pmc
import conventionalCode as cc
def main():
#file
    pokeFile = "PGenAll170719.csv"

    #fHandle
    fHandle = open(pokeFile)

    #1. generate a pokeparty, identify the individual types

    #transfers csv file info to dictionary
    pokeNameTypes_dict = {}
    pokePartyData_dict = {}

    fHandle.readline()
    for line in fHandle:
        line = cc.strNspl(line)
        pokeNameTypes_dict[line[0]] = [line[1],line[2]] #<----------------------------

    pokeParty = genPokeTeam(1, pokeFile)

    for mon in pokeParty:
        pokePartyData_dict[mon] = pokeNameTypes_dict[mon]
#checkpoint
    for mon in pokeParty:
        print(mon + " " +str(pokePartyData_dict[mon]))
#--------------
    #2. set moves
    for mon in pokeParty:
        
        nickName1 = pmc.Pokemon("Magneton")
        nickName2 = pmc.Pokemon("Ambipom")
        nickName3 = pmc.Pokemon("Hippopotas")
        nickName4 = pmc.Pokemon("Gastly")
        nickName5 = pmc.Pokemon("Vaporeon")
        nickName6 = pmc.Pokemon("Beedrill")
    pokeClass_list = [nickName1,nickName2,nickName3,nickName4,nickName5,nickName6]
    
        
    

#from pkmnTeamGenerator b/c modules cannot mutually reference each other
def genPokeTeam(num, pokeFile):
    pokeTeam_list = []
    pokeName_dict = {}

    fHandle = open(pokeFile)
    fHandle.readline()
    i = 1
    for line in fHandle:
        line = cc.strNspl(line)

        pokeName_dict[i] = line[0] #<---------------------------------------
        i += 1

    while len(pokeTeam_list) != num:
        ranVal = random.randint(1,len(pokeName_dict))
        pokeTeam_list.append(pokeName_dict[ranVal])
    return pokeTeam_list

main()
