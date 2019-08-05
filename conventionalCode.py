#Conventional user-defined functions

#---------------------------------------Misc
#adds a newline for printing
def space(num):
    print("\n"*num)




def pureTitle(s):
    s = str(s)
    first = s[:1]
    first = first.title()
    first += s[1:]
    return first

def getCase(s):
    case = ""
    s = str(s)
    if s == pureTitle(s):
        case = "title"
    elif s == s.lower():
        case = "lower"
    elif s == s.upper():
        case = "upper"
    else:
        case = "Unknown case"
    return case
#------------------------------------------error message
class CustomError(Exception):
    pass




#-------------------------------------------file functions
#strips newline and splits at ','
def strNspl(line,strp = "\n",splt = ","):
    line = line.strip(strp)
    line = line.split(splt)
    return line

#removes specific characters from a list of strings
def rem(strList, char):
    retList = []
    for i in strList:
        i = i.strip(char = "")
        retList.append(i)
    return retList

#checks if string has no empty spaces or white spaces
def isSuperEmpty(string):
    superEmpty = False
    if string.isspace():
        superEmpty = True
    elif string == "":
        superEmpty = True
    return superEmpty



#----------------------------------List functions
def hasDuplicate(alist):
    dup = False
    for a in alist:
        count = alist.count(a)
        if count > 1:
            dup = True
            break
    return dup
        
#test
##alist = [1,2,3,4,1]
##print(hasDuplicate(alist))

#searches if there's a common element from a list of lists
#assume that the elements in each list are unique
def haveCommon(listOLists):
    common = False
    allList = [*listOLists]
    allElements = []
    for l in allList:
        if hasDuplicate(l):
            raise ValueError("List contains non-unique elements.")
        else:
            allElements.extend([*l])
    if hasDuplicate(allElements):
        common = True
    return common

def removeCommon(alist):
    tempDict = {}
    retList = []
    for i in alist:
        if i not in tempDict:
            tempDict[i] = 1
    for key in tempDict.keys():
        retList.append(key)
    return retList

#test
##alist = [1,2,3,4,5]
##blist = [9,8,7,6,]
##clist = [12,13,14,15,5]
##print(haveCommon([alist,blist,clist]))

#returns all non-blank in list
def retNonBlanks(alist,blank = ""):
    retList = []
    [retList.append(x) if x != blank else x for x in alist]
    return retList

#test

##a = [1,2,3,"",4,5,""," "]
##b = retNonBlanks(a,"")
##print(b)


def hasDuplicate(alist):
    dup = False
    for a in alist:
        count = alist.count(a)
        if count > 1:
            dup = True
            break
    return dup
        
#test
##alist = [1,2,3,4,1]
##print(hasDuplicate(alist))

#function takes in a list of strings and letter case parameter and returns 
def sameCase(alist, case):
    retList = []
    case = case.lower()
    if case == "title":
        retList = [i.title() for i in alist]
    elif case == "lower":
        retList = [i.lower() for i in alist]
    elif case == "upper":
        retList = [i.upper() for i in alist]
    else:
        raise ValueError("Enter correct parameters")
    return retList
    


#function takes a list of sublists of strings and sets the proper case for each string in the sublist
#returns a list of sublists
def caseLists(alist, case):
    retList = []
    for sublist in alist:
        if case == "title":
            sublist = [x.title() for x in sublist]
        elif case == "lower":
            sublist = [x.lower() for x in sublist]
        elif case == "upper":
            sublist = [x.upper() for x in sublist]
        else:
            raise ValueError("Enter correct parameters")
        retList.append(sublist)
    return retList

#function turns lists of lists into a list of elements
#works only with one layer of list
def cascadeLists(listOfLists):
    retList = []
    for element in listOfLists:
        if not isinstance(element,list):
            retList.append(element)
        else:
            retList.extend([*element])
    return retList 

#recursively delists lists through any number of layers
def rec_cascadeLists(listOfLists):
    #checks if False is in the list comprehension
    #list comprehension checks each element in list to see if it's a list, returns False if list
    if False not in [True if not isinstance(x,list) else False for x in listOfLists]:
        return listOfLists
    else:
        return rec_cascadeLists(cascadeLists(listOfLists))

#print(rec_cascadeLists([1,2,3,[4,5,[6]]]))

#mixes the elements of a lists of lists into one list
def interMixLists(lists):
    count = len(cascadeLists(lists))
    retList = []
    j = 0
    while j != count:
        for i in range(len(lists)):
            if j < len(lists[i]):
                retList.append(lists[i][j])
            else:
                retList.append("")
        j += 1
    return retList

#---------------------------------------------tuples
    
#function turns tuples of tuples into a single tuple
def cascadeTuples(tupOfTups):
    retTup = ()
    for element in tupOfTups:
        if not isinstance(element,tuple):
            retTup += (element,)
        else:
            retTup += (*element,)
    return retTup 


#recursively detuples
def rec_cascadeTuples(tupOfTups):
    #checks if False is in the list comprehension
    #list comprehension checks each element in list to see if it's a list, returns False if list
    if False not in [True if not isinstance(x,tuple) else False for x in tupOfTups]:
        return tupOfTups
    else:
        return rec_cascadeTuples(cascadeTuples(tupOfTups))

#print(rec_cascadeTuples((1,((2,3),4,(5,6,(7))))))

#---------------------------------------------------dictionary


#-------------------------------------------------printing data
#prints relative counts
def printRel(count_dict):
    total = sum(count_dict.values())
    retDict = {}
    print("{:<20}{:<40}{:<15}".format("Key","Relative frequency","Counts"))
    for i in count_dict:
        print("{:<20}{:<40}{:<15}".format(str(i),str(count_dict[i]/total),str(count_dict[i])))
#test
count_test = {"Hello":1,"Hi":2,"Sup":3}
##printRel(count_test)

#prints Horizontal bar charts
def printHorBarChart(count_dict):
    bar = "]"
    barStr = ""
    for i in count_dict:
        barStr = bar*count_dict[i]
        print("{:<20}{:<30}".format(str(i),barStr))
#printHorBarChart(count_test)

#lazy method, not efficient
def printTop(num, count_dict, rev = True):
    top_list = [*count_dict.values()]
    top_list.sort(reverse = rev)
    top_list = top_list[:num]

    retDict = {}
    
    for j in top_list:
        for i in count_dict:
            if count_dict[i] == j and i not in retDict:
                #retDict[i] = j
                print("{:<20}{:<30}".format(str(i),j))

#printTop(3,count_test)

    




