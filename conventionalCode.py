#Conventional user-defined functions

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

#adds a newline for printing
def space(num):
    print("\n"*num)

#returns all non-blank in list
def retNonBlanks(alist,blank = ""):
    retList = []
    [retList.append(x) if x != blank else x for x in alist]
    return retList

#test

##a = [1,2,3,"",4,5,""," "]
##b = retNonBlanks(a,"")
##print(b)


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

    




