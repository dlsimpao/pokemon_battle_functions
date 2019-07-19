#Pokedata
#central module for all Pokemon data
import conventionalCode as cc


#Pokemon name and type 
pokeFile_dict = {"Pokemon":"PGenAll170719.csv", "Moves":"PokeAttackdex.csv"}
#fHandle = open(pokeFile)
    

def getFHandle(pokeFilePar):
    try:
        pokeFilePar = pokeFilePar.title()
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
    #fHandle = getFHandle(fHandle)
    retDict = {}
    coln_dict = {}

    if selectedColn_list != []:
        header = True
        
    if header:
        hdr = getHeader(fHandle)
        for name in selectedColn_list:
            if name not in hdr:
                print(str(name)+" is not a valid column name.")
                print("Please select from: "+str(hdr))
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
            retDict[line[0]] = tuple(line[1:])
        #if the first column is selected
        elif hdr[0] in selectedColn_list:
            for name in selectedColn_list[1:]:
                if line[0] not in retDict:
                    retDict[line[0]] = line[coln_dict[name]]
                else:
                    oldColn = retDict.get(line[0])
                    newColn = line[coln_dict[name]]
                    comColn = cc.rec_cascadeTuples((oldColn,newColn))
                    retDict[line[0]] = comColn
        else:
            moreColn = ()
            for name in selectedColn_list:
                if i not in retDict:
                    retDict[i] = line[coln_dict[name]]
                else:
                    oldColn = retDict.get(i)
                    newColn = line[coln_dict[name]]
                    comColn = cc.rec_cascadeTuples((oldColn,newColn))
                    retDict[i] = comColn
            i += 1
    return retDict


#summarizes single and dual types
#summarizes type relativity
def pokeTypeSummary():
    #fHandle = getFHandle("Pokemon")
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
        distType_list = []
        
        for key in types_dict:
           if types_dict[key] not in distType_list:
               distType_list.append(types_dict[key])
               
    elif fHandle.title() == "Pokemon":
        fHandle = getFHandle("Pokemon")
        types_dict = autoDict(fHandle, ["Type I", "Type II"])
        distType_list = []

        for key in types_dict:
            if types_dict[key] not in distType_list:
                distType_list.append(types_dict[key])
                
    return distType_list


#problem: unhashable type 'list' occurs when I try to count the distinct number of dual types
def countDistinct(fHandle):
    count_dict = {}
    type_dict = autoDict(fHandle)

    for types in type_dict:
##        if isinstance(type_dict[types],list):
##                type_dict[types] = tuple(type_dict[types])
        if type_dict[types] not in count_dict:
            count_dict[type_dict[types]] = 1
        else:
            count_dict[type_dict[types]] += 1
    return count_dict

def printRel(count_dict):
    totCount = sum(count_dict.values())
    retDict = {}
    for i in count_dict:
        print(i[:3]+"\t{:.2f}".format((count_dict[i]/totCount),3)+"\t"+\
              str(count_dict[i]))
        
        
    
    
