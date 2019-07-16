#Pokemon Matchup test generator
#FOR GEN I ONLY

#later include choice between a combination of generations and all
#include other gen csv files and also master file

genFile = "PGen1.csv"

#dictionaries with values based on 
gen1Pokenum_dict = {}
gen1Pokename_dict = {}

num, name, hp, atk, dfn, spa, spd, tot, type1, type2 = 0,0,0,0,0,0,0,0,0,0

fHandle = open(genFile, "r")
fHandle.readline()
for line in fHandle:

    line = line.strip('\n')
    #print(line)

    #list of Pokemon's stats
    line = line.split(',',2)
    print(line)
    
    gen1Pokenum_dict[line[0]] = [line[2],line[3],line[4],line[5],line[6],line[7],line[8]]
    gen1Pokename_dict[line[1]] = [line[2],line[3],line[4],line[5],line[6],line[7],line[8]]
#print(line)

for key in gen1Pokenum_dict:
    print(key)



