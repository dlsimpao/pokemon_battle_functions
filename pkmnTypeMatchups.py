#P-Type Counters - generates type matchups and move effectiveness
# to work, uncomment main() below

import conventionalCode as cc
import pkmnData as pd


def main():
    type_list = ["normal","fighting","flying","poison","ground","rock","bug","ghost","steel",\
                 "fire","water","grass","electric","psychic","ice","dragon","dark","fairy"]
    
    #Asks user for types and stores in choice list
    choice_list = askForTypes(type_list)

    #formats choice list into 
    choice_list = [type1.lower() for type1 in choice_list]

    #checks if user wants 
    ans2 = choiceCheck1(choice_list)
    while ans2 == "yes":
        main()

    printEffectReport(choice_list)


#choice check1
def choiceCheck1(choice_list):
    ans2 = input("You have chosen: "+str(choice_list)+"\nDo you want to change your choice? Yes | No?\n")
    if ans2.lower() == "yes":
        main()
    elif ans2.lower() == "no":
        pass
    else:
        print("Please enter a valid answer")
        choiceCheck1(choice_list)
        
#identifies valids from user input; returns a list of valid types
def askForTypes(type_list):
    ans1 = input("Please enter up to two different valid types.\n")
    validInputs = []
    while ans1 != '' and (len(validInputs) < 3) :
        if isValidType(ans1,type_list) and ans1 not in validInputs:
            validInputs.append(ans1)
        ans1 = input()
    return validInputs
    
    
#checks if valid type
#improve to include valid dual types
def isValidType(type1,typeList):
    valid = False
    try:
        type1 = type1.lower()
        if type1 in typeList:
            valid = True      
    except:
        raise ValueError
    else:
        if type1 not in typeList:
            print("Please enter valid types from this list:\n")
            for i in range(len(typeList)):
                print(typeList[i])
            main()
        else:
            pass
    return valid

#--------------------------------------------------------------create an isValidDualType

## type_list = ["normal","fighting","flying","poison","ground","rock","bug","ghost","steel"\
##                 "fire","water","grass","electric","psychic","ice","dragon","dark","fairy","none",None]

##if type1 in type_list and typ2 in type_list:
##            type1.lower()
##            if type2 != None:
##                type2.lower()
##            valid = True

def getMoveTypeEffects(type_num, types_dict):
    noEffectAgainst = []
    notVeryEffectiveAgainst = []
    effectiveAgainst = []

    type_num = type_num.lower()
    
    for key in types_dict[type_num]:
        if types_dict[type_num][key] == 0:
            noEffectAgainst.append(key)
        elif types_dict[type_num][key] == 0.5:
            notVeryEffectiveAgainst.append(key)
        elif types_dict[type_num][key] == 2:
            effectiveAgainst.append(key)
    return noEffectAgainst,notVeryEffectiveAgainst,effectiveAgainst

def printMoveTypeReport(type_num,types_dict):
    noEffectAgainst,notVeryEffectiveAgainst,effectiveAgainst = getMoveTypeEffects(type_num,types_dict)
    print("------------------------------------------------------------------------------------------------------\n"\
          "----------------------------------------Move Type Report----------------------------------------------")
    print(type_num+"-type moves\n\n"+\
          "-have no effect against:"+str(noEffectAgainst)+"\n"+\
          "-are not very effective against:"+str(notVeryEffectiveAgainst)+"\n"+\
          "-are super effective against:"+str(effectiveAgainst))


#creates a temp dictionary by filling out matchup effect values of ones
def valAssgn(type1,type2,types_dict):
    for key in types_dict:
        if type1 not in types_dict[key]:
            types_dict[key][type1] = 1
        if type2 not in types_dict[key]:
            types_dict[key][type2] = 1
    

#prints the matchups based on effectiveness
def printMatchupReport(choice_list):
    immuneAgainst, superResistantAgainst, resistantAgainst, weakAgainst,superWeakAgainst = getEffectMatch(choice_list)
    try:
        type1 = choice_list[0]
        type2 = choice_list[1]
        
    except:
        pass
        
    if len(choice_list) == 1:
        print("------------------------------------------------------------------------------------------------------\n"\
              "----------------------------------------Matchup Report----------------------------------------------")
        print(type1+"-types\n\n"+\
              "-are immune against"+str(immuneAgainst)+"\n"+\
              "-are resistant against:"+str(resistantAgainst)+"\n"+\
              "-are weak against:"+str(weakAgainst))
    else:
        print("------------------------------------------------------------------------------------------------------\n"\
              "----------------------------------------Matchup Report----------------------------------------------")
        print(type1+"-"+type2+" types\n\n"+\
              "-are immune against"+str(immuneAgainst)+"\n"+\
              "-are super resistant against"+str(superResistantAgainst)+"\n"+\
              "-are resistant against:"+str(resistantAgainst)+"\n"+\
              "-are weak against:"+str(weakAgainst)+"\n"+\
              "-are super weak against:"+str(superWeakAgainst))

#retuns lists of the chosen types' varying matchups
def getEffectMatch(choice_list):
    choice_list = [x.lower() for x in choice_list]
    
    types_dict = pd.getTypes_dict
    
    #for dual types
    superResistantAgainst = []
    superWeakAgainst = []

    
    #type matchup
    weakAgainst = []
    resistantAgainst = []
    immuneAgainst = []
    
    if len(choice_list) == 1:
        type1 = choice_list[0]
        for key in types_dict:
            try:
                if types_dict[key][type1] == 0:
                    immuneAgainst.append(key)
                elif types_dict[key][type1] == 0.5:
                    resistantAgainst.append(key)
                elif types_dict[key][type1] == 2:
                    weakAgainst.append(key)
            except:
                pass

    else:
        type1, type2 = choice_list[0],choice_list[1]
        valAssgn(type1,type2,types_dict)
        for key in types_dict:
            if types_dict[key][type1]*types_dict[key][type2] == 0:
                immuneAgainst.append(key)
            elif types_dict[key][type1]*types_dict[key][type2] == 0.25:
                superResistantAgainst.append(key)
            elif types_dict[key][type1]*types_dict[key][type2] == 0.5:
                resistantAgainst.append(key)
            elif types_dict[key][type1]*types_dict[key][type2] == 2:
                weakAgainst.append(key)
            elif types_dict[key][type1]*types_dict[key][type2] == 4:
                superWeakAgainst.append(key)
    return immuneAgainst, superResistantAgainst, resistantAgainst, weakAgainst,superWeakAgainst
    



#prints report
def printEffectReport(choice_list): 

    #dictionary of all type effects
    types_dict = pd.getTypes_dict()
    #prints reports depending on single and dual type
    #---------------------------------------separate the print reports
    if len(choice_list) == 2:
        type1, type2 = choice_list[0],choice_list[1]
        printMoveTypeReport(type1,types_dict)
        printMoveTypeReport(type2,types_dict)

        printMatchupReport(choice_list)
    else:
        type1 = choice_list[0]
        printMoveTypeReport(type1,types_dict)
        printMatchupReport(choice_list)

    

    
#main()
#printEffectReport(["Fire","Flying"])
#printEffectReport(["Fire"])
