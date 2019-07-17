#random Pokemon party generator
#create optimal team generator (instead of random)

import random

def genPokeTeam():
    pokeTeam_list = []
    pokeName_dict = {}

    fHandle = open("PGenALL170719.csv")
    fHandle.readline()
    i = 1
    for line in fHandle:
        line = line.strip("\n")
        line = line.split(",")

        pokeName_dict[i] = line[0]
        i += 1

    while len(pokeTeam_list) != 6:
        ranVal = random.randint(1,len(pokeName_dict))
        pokeTeam_list.append(pokeName_dict[ranVal])
    return pokeTeam_list

##alist = genPokeTeam()
##print(alist)

