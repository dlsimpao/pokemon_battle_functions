#Pokedata
#central module for all Pokemon data
import conventionalCode as cc
import fileinput

#Pokemon name and type 
pokeFile_dict = {"Pokemon":"PGenAll170719.csv", "Moves":"PokeAttackdex.csv"}
#fHandle = open(pokeFile)
    

def getFHandle(pokeFilePar, action = "r"):
    try:
        pokeFilePar = pokeFilePar.title()
        pokeFile = pokeFile_dict[pokeFilePar]
        fHandle = open(pokeFile, action)
    except:
        print("Please enter a valid file name:")
        for file in pokeFile_dict:
            print(file)
        print("Try typing a valid action: w+, w, r, a+")
        exit()
    return fHandle

def getFileName(pokeFilePar):
    fileName = ""
    try:
        pokeFilePar = pokeFilePar.title()
        fileName = pokeFile_dict[pokeFilePar]
    except:
        print("Please enter a valid file name:")
        for file in pokeFile_dict:
            print(file)
    return fileName

def getHeader(fHandle):
    header = fHandle.readline()
    header = cc.strNspl(header)
    return header


def printData(fHandle):
    for line in fHandle:
        line = cc.strNspl(line)
        print(line)

##def writeHeader(pokeFilePar):
##    headerStr = ""
##    header = []
##    #not all lines have filled column values and thus, may vary
##    #maxcolnCount keeps track of the largest column entries of any line
##    
##    fHandle = getFHandle(pokeFilePar, action = "r")
##    hdrCount = len(getHeader(fHandle))
##    fHandle = getFHandle(pokeFilePar, action = "a+")
##    
##    while len(header) < hdrCount:
##        hdrName = input("Please enter header name for column "+str(len(header)+1)+"/"+str(hdrCount)+":\n")
##        header.append(hdrName)
##
##    for hdrName in header:
##        headerStr += str(hdrName)+", "
##    fHandle.write(headerStr)
##    fHandle.close()
##

    

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
def countDistinct(poke_dict):
    count_dict = {}
    
    for types in poke_dict:
##        if isinstance(type_dict[types],list):
##                type_dict[types] = tuple(type_dict[types])
        if poke_dict[types] not in count_dict:
            count_dict[poke_dict[types]] = 1
        else:
            count_dict[poke_dict[types]] += 1
    return count_dict




    
