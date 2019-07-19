#Pokemon party generator
#possible additions
#1. Optimized Pokemon party gen
#2. Guided Pokemon party creator
#3. Themed Party gen

import conventionalCode as cc
import random

def genPokeTeam(num):
    pokeTeam_list = []
    pokeName_dict = {}

    fHandle = open("PGenALL170719.csv")
    fHandle.readline()
    i = 1
    for line in fHandle:
        line = cc.strNspl(line)

        pokeName_dict[i] = line[0]
        i += 1

    while len(pokeTeam_list) != num:
        ranVal = random.randint(1,len(pokeName_dict))
        pokeTeam_list.append(pokeName_dict[ranVal])
    return pokeTeam_list

alist = genPokeTeam(6)
print(alist)

