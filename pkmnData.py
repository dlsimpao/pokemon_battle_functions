#Pokedata
#central module for all Pokemon data
import conventionalCode as cc
import fileinput


#Pokemon name and type 
pokeFile_dict = {"Pokemon":"allPkmnGen1-7.csv", "Moves":"PokeAttackdex.csv"}
#fHandle = open(pokeFile)

typesMatchup_dict = {'Normal': {'Rock': 0.5, 'Ghost': 0, 'Steel': 0.5},\
                     'Fighting': {'Normal': 2, 'Flying': 0.5, 'Poison': 0.5, 'Rock': 2, 'Bug': 0.5, 'Ghost': 0, 'Steel': 2, 'Psychic': 0.5, 'Ice': 2, 'Dark': 2, 'Fairy': 0.5},\
                     'Flying': {'Fighting': 2, 'Rock': 0.5, 'Bug': 2, 'Steel': 0.5, 'Grass': 2, 'Electric': 0.5},\
                     'Poison': {'Poison': 0.5, 'Ground': 0.5, 'Rock': 0.5, 'Ghost': 0.5, 'Steel': 0, 'Grass': 2, 'Fairy': 2},\
                     'Ground': {'Flying': 0, 'Poison': 2, 'Rock': 2, 'Bug': 0.5, 'Steel': 2, 'Fire': 2, 'Grass': 0.5, 'Electric': 2},\
                     'Rock': {'Fighting': 0.5, 'Flying': 2, 'Ground': 0.5, 'Bug': 2, 'Steel': 0.5, 'Fire': 2, 'Ice': 2},\
                     'Bug': {'Fighting': 0.5, 'Flying': 0.5, 'Poison': 0.5, 'Ghost': 0.5, 'Steel': 0.5, 'Fire': 0.5, 'Grass': 2, 'Psychic': 2, 'Dark': 2, 'Fairy': 0.5},\
                     'Ghost': {'Normal': 0, 'Ghost': 2, 'Psychic': 2, 'Dark': 0.5},\
                     'Steel': {'Rock': 2, 'Steel': 0.5, 'Fire': 0.5, 'Water': 0.5, 'Electric': 0.5, 'Ice': 2, 'Fairy': 2},\
                     'Fire': {'Rock': 0.5, 'Bug': 2, 'Steel': 2, 'Fire': 0.5, 'Water': 0.5, 'Grass': 2, 'Ice': 2, 'Dragon': 0.5},\
                     'Water': {'Ground': 2, 'Rock': 2, 'Fire': 2, 'Water': 0.5, 'Grass': 0.5, 'Dragon': 0.5},\
                     'Grass': {'Flying': 0.5, 'Poison': 0.5, 'Ground': 2, 'Rock': 2, 'Bug': 0.5, 'Steel': 0.5, 'Fire': 0.5, 'Water': 2, 'Grass': 0.5, 'Dragon': 0.5},\
                     'Electric': {'Flying': 2, 'Ground': 0, 'Water': 2, 'Grass': 0.5, 'Electric': 0.5, 'Dragon': 0.5},\
                     'Psychic': {'Fighting': 2, 'Poison': 2, 'Steel': 0.5, 'Psychic': 0.5, 'Dark': 0},\
                     'Ice': {'Flying': 2, 'Ground': 2, 'Steel': 0.5, 'Fire': 0.5, 'Water': 0.5, 'Grass': 2, 'Ice': 0.5, 'Dragon': 2},\
                     'Dragon': {'Steel': 0.5, 'Dragon': 2, 'Fairy': 0},\
                     'Dark': {'Fighting': 0.5, 'Ghost': 2, 'Psychic': 2, 'Dark': 0.5, 'Fairy': 0.5}, \
                     'Fairy': {'Fighting': 2, 'Poison': 0.5, 'Steel': 0.5, 'Fire': 0.5, 'Dragon': 2, 'Dark': 2}}




##def titleDic(dic):
##    ret_dict = {}
##    for key in dic:
##        ret_dict[key.title()] = dic[key]
##    return ret_dict
##
##def titleDic2(dic):
##    ret_dict = {}
##    for key in dic:
##        ret_dict[key.title()] = titleDic(dic[key])
##    return ret_dict
##print(titleDic2(typesMatchup_dict))
    
    
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

#creates a dictionary based on a given list of column names
def autoDict(fHandle, selectedColn_list = [], index = True):
    #fHandle = getFHandle(fHandle)
    retDict = {}
    coln_dict = {}
        
    #For now, I assume, a header is given for all files
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
        elif hdr[0] in selectedColn_list and index == False:
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


def getPkmnTypes(pkmn):
    pkmn = cc.pureTitle(pkmn)
    return pkmnTypes_dict[pkmn]

def getPkmnMoveType(move):
    move = cc.pureTitle(move)
    return pkmnMoveType_dict[move].title()
    
def getDistinctTypes(fh):
    fh = fh.title()
    distType_list = []
    if fh == "Moves":
        fHandle = getFHandle("Moves")
        types_dict = autoDict(fHandle, ["Type"])
        
        for move,type1 in types_dict.items():
           if type1 not in distType_list:
               distType_list.append(type1)
               
    elif fh == "Pokemon":
        fHandle = getFHandle("Pokemon")
        types_dict = autoDict(fHandle, ["Type I", "Type II"])

        for pkmn,types in types_dict.items():
            if types not in distType_list:
                distType_list.append(types)
                
    return distType_list



def getDistinct(poke_dict):
    count_dict = {}
    
    for types in poke_dict:
##        if isinstance(type_dict[types],list):
##                type_dict[types] = tuple(type_dict[types])
        if poke_dict[types] not in count_dict:
            count_dict[poke_dict[types]] = 1
        else:
            count_dict[poke_dict[types]] += 1
    return count_dict

#function returns all moves of a certain type, given a list
def getAllMoves(moveTypes = []):
    retDict = {}

    for move,type1 in pkmnMoveType_dict.items():
        if type1 in moveTypes:
            if type1 not in retDict:
                retDict[type1] = move
            else:
                oldMove = retDict.get(type1)
                newMoves = [oldMove,move]
                newMoves = cc.cascadeLists(newMoves)
                retDict[type1] = newMoves
    return retDict

#function returns the counts of all the moves per type, given a dictionary type as key, list of moves as value
def getCounts(pkmnTMoves_dict):
    retDict = []
    for moveType,moves in pkmnTMoves_dct.items():
        retDict[moveType] = len(moves)
    return retDict

#modify to go beyond two types
def printAllMoves(moveTypes = []):
    i = 0

    #string to print
    prStr = ""

    #list with all caps types
    moveTypes = [x.upper() for x in moveTypes]
    
    #dictionary, key = type, value = list of moves
    moveDict = getAllMoves(moveTypes)
    
    #list of all moves from moveDict
    move_lists = list(moveDict.values())
    #combines all list such as [a1,b1,c1...] from list a,b,c
    alist = cc.interMixLists(move_lists)

    #formats for titles
    helpStr = "{:<30}"*len(moveTypes)

    #list for header
    title_list = []

    for j in range(len(moveTypes)):
        title_list.append(pkmnMoveType_dict[alist[j]])
        
    movesCount = len(cc.cascadeLists(move_lists))

    print(helpStr.format(*title_list))
    while i < movesCount:
        for m in range(len(move_lists)):
            if m == len(move_lists)-1:
                prStr += alist[i]+"\n"
            else:
                prStr += "{:<30}".format(alist[i])
            i += 1
    print(prStr)

#------------------------------------------------

fHandle = getFHandle("Pokemon")
pkmnTypes_dict = autoDict(fHandle)

fHandle2 = getFHandle("Moves")
pkmnMoveType_dict = autoDict(fHandle2,["Name","Type"],index = False)




type_list = []
for key in typesMatchup_dict:
    type_list.append(key)

#-------------------------------------------------------------

