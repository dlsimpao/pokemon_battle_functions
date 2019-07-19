#Conventional user-defined functions

#strips newline and splits at ','
def strNspl(line):
    line = line.strip("\n")
    line = line.split(",")
    return line

#adds a space/s for printing
def space(num):
    print("\n"*num)

#returns all non-blank in  list
def retNonBlanks(alist,blank = ""):
    retList = []
    for element in alist:
        if element != blank:
            retList.append(element)
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
    totCount = sum(count_dict.values())
    retDict = {}
    for i in count_dict:
        print("{:<20}".format(str(i))+"\t{:^15}".format("{:.4f}".format((count_dict[i]/totCount)),3)+"\t"+\
              "{:^15}".format(str(count_dict[i])))

#prints Horizontal bar charts
def printHorBarChart(count_dict):
    bar = "]"
    barStr = ""
    for i in count_dict:
        barStr = bar*count_dict[i]
        print("{:<20}".format(str(i))+"\t{:<30}".format(barStr))

#lazy method, not efficient
def printTop(num, count_dict):
    top_list = [*count_dict.values()]
    top_list.sort(reverse = True)
    top_list = top_list[:num]

    retDict = {}
    
    for j in top_list:
        for i in count_dict:
            if count_dict[i] == j and i not in retDict:
                #retDict[i] = j
                print("{:<20}".format(str(i))+"\t{:<30}".format(j))

    




