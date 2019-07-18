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

#function takes a list of sublists of strings and capitalizes the first letter each string in the sublist
#returns a list of sublists
def capLists(alist):
    retList = []
    for sublist in alist:
        sublist = [x.title() for x in sublist]
        retList.append(sublist)
    return retList
