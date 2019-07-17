#Pokemon Matchup test generator
#FOR GEN I ONLY

import TypeMatchups as tm

#later include choice between a combination of generations and all
#include other gen csv files and also master file

genFile = "PGen1.csv"

#dictionaries with values based on 
#not in use#gen1Pokenum_dict = {}
gen1Pokename_dict = {}



fHandle = open(genFile, "r")
header = fHandle.readline()
header = header.strip('\n')
header = header.split(',')

for line in fHandle:

    line = line.strip('\n')

    #list of Pokemon's stats
    line = line.split(',')

    #dictionary of dictionaries
    
    #not in use#gen1Pokenum_dict[line[0]] = [line[2],line[3],line[4],line[5],line[6],line[7],line[8],line[9]]
    gen1Pokename_dict[line[1]] = {header[0]:line[0],header[2]:line[2],header[3]:line[3],header[4]:line[4],\
                                  header[5]:line[5],header[6]:line[6],header[7]:line[7],header[8]:line[8],\
                                  header[9]:line[9], header[10]:line[10]}


for key in gen1Pokename_dict:
    print(key)

pokeName = "charizard".title()
pokeTypes = [gen1Pokename_dict[pokeName]["Type I"],gen1Pokename_dict[pokeName]["Type II"]]

if pokeName in gen1Pokename_dict:
    printStr = ""
    if pokeTypes[1] == "":
        printStr = pokeName+" is a "+pokeTypes[0]+" type Pokemon"
    else:
        printStr = pokeName+" is a "+pokeTypes[0]+"-"+pokeTypes[1]+\
                   " Dual type Pokemon."
print(printStr)

#specify which Pokemon generation
pokeGen = 1

tm.printEffectReport(pokeTypes)




