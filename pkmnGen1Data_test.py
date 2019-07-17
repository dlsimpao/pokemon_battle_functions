#Pokemon Matchup test generator 
#FOR GEN I ONLY

#some faults:
#The evaluation of the matchup only takes into account the Pokemon's type
#and not move types
#It's not that helpful practically

import TypeMatchups as tm

#later include choice between a combination of generations and all
#include other gen csv files and also master file



#function takes a list of sublists of strings and capitalizes each string in the sublist
#returns a list of sublists
def capLists(alist):
    retList = []
    for sublist in alist:
        sublist = [x.title() for x in sublist]
        retList.append(sublist)
    return retList

##def strNspl(line, strChar, splChar):
##    line = line.strip('\n')
##    line = line.split(',')
##    return line
    
#doc name
genFile = "PGen1.csv"

#dictionaries with values based on 
#not in use#gen1Pokenum_dict = {}
gen1Pokename_dict = {}


#creates filehandle
fHandle = open(genFile, "r")

#takes the header
header = fHandle.readline()
header = header.strip('\n')
header = header.split(',')

#gets data from the filehandle

for line in fHandle:

    line = line.strip('\n')

    #list of Pokemon's stats
    line = line.split(',')

    #dictionary of dictionaries
    
    #not in use#gen1Pokenum_dict[line[0]] = [line[2],line[3],line[4],line[5],line[6],line[7],line[8],line[9]]
    gen1Pokename_dict[line[1]] = {header[0]:line[0],header[2]:line[2],header[3]:line[3],header[4]:line[4],\
                                  header[5]:line[5],header[6]:line[6],header[7]:line[7],header[8]:line[8],\
                                  header[9]:line[9], header[10]:line[10]}

#Pokemon in dictionary
##for key in gen1Pokename_dict:
##    print(key)




    #---------------------------------------------------------------------------------------

pokeName = "Onix".title()

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
immune, supRes, res, weak, supWeak = tm.getEffectMatch(pokeTypes)
effect_list = [immune, supRes, res, weak, supWeak]
effect_list = capLists(effect_list)
#print(effect_list)

gMatchTo,bMatchTo,sBMatchTo = [], [], []

for key in gen1Pokename_dict:
    for i in range(len(effect_list)):
        if gen1Pokename_dict[key]["Type I"] in effect_list[i]:
            if i < 3:
                gMatchTo.append(key)
            elif i == 4:
                bMatchTo.append(key)
            else:
                sBMatchTo.append(key)

print("Considering all gen 1 Pokemon, "+pokeName+" has a defensively \n\ngood matchup to:"+str(gMatchTo)+\
      "\n\nbad matchup to:"+str(bMatchTo)+\
      "\n\nreally bad matchup to:"+str(sBMatchTo))
    
    




