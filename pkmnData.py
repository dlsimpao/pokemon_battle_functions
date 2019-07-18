#Pokedata
#central module for all Pokemon data
import conventionalCode as cc

#Pokemon name and type 
pokeFile_dict = {"Pokemon":"PGenAll170719.csv", "Moves":"PokeAttackdex.csv"}
#fHandle = open(pokeFile)
    

def getFHandle(pokeFilePar):
    try:
        pokeFile = pokeFile_dict[pokeFilePar]
        fHandle = open(pokeFile)
    except:
        print("Please enter a valid file name:")
        for file in pokeFile_dict:
            print(file)
        exit()
    return fHandle
    

def getHeader(fHandle):
    header = fHandle.readline()
    header = cc.strNspl(header)
    return header


def printData(fHandle):
    for line in fHandle:
        line = cc.strNspl(line)
        print(line)

#automatically assumes 1st column as the keys to the dictionary
def autoDict(fHandle, selectedColn_list = [], header = True):
    retDict = {}
    coln_dict = {}

    if selectedColn_list != []:
        header = True
        
    if header:
        hdr = getHeader(fHandle)
        for name in selectedColn_list:
            if name not in hdr:
                print(str(name)+" is not a valid column name.")
                break
        c = 0 #column dictionary index
        for name in hdr:
            coln_dict[name] = c
            c += 1
                      
    i = 0 #specific column index
    for line in fHandle:
        line = cc.strNspl(line)
        #if no columns are selected
        if selectedColn_list == []:
            retDict[line[0]] = line[1:]
        #if the first column is selected
        elif hdr[0] in selectedColn_list:
            for name in selectedColn_list:
                selected = []
                if name not in selected:
                    retDict[line[0]] = line[coln_dict[name]]
                    selected.append(name)
                else:
                    selected = [retDict.get(i)]
                    selected.append(line[0])
                    selected = cc.rec_cascadeLists(selected)
                    retDict[line[0]] = selected
        #if any but the first column is selected
        else:
            selected = []

            for name in selectedColn_list:
                if i not in retDict:
                    retDict[i] = line[coln_dict[name]]
                else:
                    selected = [retDict.get(i)]
                    selected.append(line[coln_dict[name]])
                    retDict[i] = selected
            i += 1


    return retDict


#summarizes single and dual types
#summarizes type relativity
def pokeTypeSummary():
    fHandle = getFHandle("Pokemon")
    type_dict = autoDict(fHandle)
    dualTypeCount = 0
    for mon in type_dict:
        if type_dict[mon][1] == "":
            dualTypeCount += 1
    
    #print(findDistinctTypes(type

def findDistinctTypes(fHandle):
    #fHandle = getFHandle("Moves")
    if fHandle.title() == "Moves":
        fHandle = getFHandle("Moves")
        types_dict = autoDict(fHandle, ["Type"])
        print(types_dict)
        distType_list = []
        
        for key in types_dict:
           if types_dict[key] not in distType_list:
               distType_list.append(types_dict[key])
               
    elif fHandle.title() == "Pokemon":
        fHandle = getFHandle("Pokemon")
        types_dict = autoDict(fHandle, ["Type I", "Type II"])
        print(types_dict)
        distType_list = []

        for key in types_dict:
            if types_dict[key] not in distType_list:
                distType_list.append(types_dict[key])
                
    return distType_list
                
    
    
