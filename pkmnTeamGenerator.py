#random Pokemon party generator


import PBattleSim as pbsim
import random

def genPokeTeam():
    pokeTeam_list = []
    pokeName_dict = {}

    fHandle = open("PGenALL170719.csv")
    fHandle.readline()
    i = 1
    for line in fHandle:
        line = pbsim.strNspl(line)
        pokeName_dict[i] = line[0]
        i += 1

    while len(pokeTeam_list) != 6:
        ranVal = random.randint(1,len(pokeName_dict))
        pokeTeam_list.append(pokeName_dict[ranVal])
    return pokeTeam_list

