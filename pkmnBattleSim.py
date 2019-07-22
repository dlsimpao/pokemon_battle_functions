#Pokemon Battle Simulation Test

import PMonsterClass as pmc
import TypeMatchups as tm
import pkmnTeamGenerator as ptg
import conventionalCode as cc

def main():
    #handle string containing Pokemon types from all nations
    dataStr = "PGenAll170719.csv"
    #national Pokemon Dictionary
    
    natPokeType_dict = createTypeDict(dataStr)

    #max six Pokemon in a party
    num = 6
##    myPokeParty = ptg.genPokeTeam(num)
##    oppPokeParty = ptg.genPokeTeam(num)

    myPokeParty = ["Hitmonlee","Primeape","Articuno","Elgyem","Rowlet","Gastrodon"]
    oppPokeParty = ["Weavile","Sneasel","Krabby","Starly","Leafeon","Basculin"]

    #printParty(myPokeParty,natPokeType_dict)
    #stores the optimal party setup, assuming no switches and advantage based solely on type

    #Mine
    myOptParty = optimizeParty(myPokeParty,oppPokeParty,natPokeType_dict)
    strongOpp = identifyStrongOpp(myOptParty, oppPokeParty)

    #Opp
    oppOptParty = optimizeParty(oppPokeParty, myPokeParty,natPokeType_dict)
    strongMine = identifyStrongOpp(oppOptParty, myPokeParty)

    printParty(myPokeParty,natPokeType_dict)
    cc.space(2)
    printParty(oppPokeParty,natPokeType_dict)
    cc.space(2)
    printFavorMatch(myOptParty, strongMine)
    cc.space(2)
    printAvoidMatch(oppOptParty)

    
    


#opens Pokemon Database
def createTypeDict(handleStr):
    pokeType_dict = {}
    fHandle = open("PGenAll170719.csv")
    header = fHandle.readline()
    header = cc.strNspl(header)
    for line in fHandle:
        line = cc.strNspl(line)
        pokeType_dict[line[0]] = [line[1],line[2]]
    return pokeType_dict

#gets Pokemon's type based on name
def getType(pokeName, type_dict):
    return type_dict[pokeName]

def printParty(party_list,type_dict):
    for mon in party_list:
        types_list = getType(mon,type_dict)
        if len(types_list) == 1:
            types_str = str(types_list)
        else:
            types_str = str(types_list[0])+" "+str(types_list[1])
        print(mon+": "+types_str)

#Given I know opponent's lineup, I optimize my party's order (based on type, not move types)
def optimizeParty(party_list,opp_list,type_dict):
    myTypes_dict = {}
    oppTypes_dict = {}
    oppTypesMatchup = {}
    #dictionary for my best line up based on order and pokemon type
    myOptLineUp = {}
    
    for mon in party_list:
        myTypes_dict[mon] = getType(mon,type_dict)
    #print("My Pokemon: "+str(myTypes_dict))
    for mon in opp_list:
        oppTypes_dict[mon] = getType(mon,type_dict)
    #cc.space(3)
    #print("Opposing Pokemon: "+str(oppTypes_dict))

    #for each pokemon in opponents party, find their matchup effectiveness
    for mon in oppTypes_dict:
        immuneAgainst, superResistantAgainst, resistantAgainst, weakAgainst,superWeakAgainst = tm.getEffectMatch(oppTypes_dict[mon])
        effect_list = cc.capLists([immuneAgainst, superResistantAgainst, resistantAgainst, weakAgainst,superWeakAgainst])
        oppTypesMatchup[mon] = effect_list
    #cc.space(3)
    
    #print(oppTypesMatchup) #test
    #cc.space(3)
    #print(oppTypesMatchup["Sneasel"][4])
    #given each opposing pokemon's weakness, arrange my party strategically
    #for each pokemon in opponent's party
    for oppMon in oppTypesMatchup:
        #for each type the opponent is weak
        for oppTypes in oppTypesMatchup[oppMon][4]:
            #for each pokemon in my party
            for myMon in myTypes_dict:   
                #if the opponent is weak against a type of Pokemon (based purely on type)
                if oppTypes in myTypes_dict[myMon]:
                    if myMon not in myOptLineUp:
                        myOptLineUp[myMon] = oppMon
                    else:
                        #resets lists
                        oppList = [myOptLineUp.get(myMon)]
                        oppList = cc.rec_cascadeLists(oppList)
                        if oppMon not in oppList:
                            oppList += [oppMon]
    
                        #adds to dictionary
                        myOptLineUp[myMon] = oppList
        for oppTypes in oppTypesMatchup[oppMon][3]:
            #for each pokemon in my party
            for myMon in myTypes_dict:   
                if oppTypes in myTypes_dict[myMon]:
                    if myMon not in myOptLineUp:
                        myOptLineUp[myMon] = oppMon
                    else:
                        #resets lists
                        oppList2 = []
##                        if isinstance(myOptLineUp.get(myMon),list):
##                            oppList2 = myOptLineUp.get(myMon)
##                        else:
##                            oppList2.append(myOptLineUp.get(myMon))
                        #adds new info
                        #resets lists
                        oppList2 = [myOptLineUp.get(myMon)]
                        oppList2 = cc.rec_cascadeLists(oppList2)
                        if oppMon not in oppList2:
                            oppList2 += [oppMon]
                        #adds to dictionary
                        myOptLineUp[myMon] = oppList2
    print(myOptLineUp)#does not work
    cc.space(3)
    return myOptLineUp
    #NEXT: normal opposition, matchups to avoid
    #NEXT: get and print functions

#identifies which opposing Pokemon will go evenly or better than mine
#given my optimal lineup dictionary and opponents' list
def identifyStrongOpp(myOpt_dict, oppList):
    retList = oppList
    #for each opposing pokemon
    for oppMon in oppList:
        for mon in myOpt_dict:
            #if any of my Pokemon has an advantage over opposing, remove from retList
            if oppMon in myOpt_dict[mon]:
                #remove if valid
                if oppMon in retList:
                    #if Pokemon in retList, replace with ""
                    retList = ["" if x == oppMon else x for x in retList]
    retList = cc.retNonBlanks(retList)
    return retList

#prints desired matchups
def printFavorMatch(myOpt_dict, strongPoke):
    for mon in myOpt_dict:
        print("My "+mon+": Use against:"+str(myOpt_dict[mon]))
    print("Opposing team has no type counter for"+str(strongPoke))


#prints unwanted matchups
def printAvoidMatch(oppOpt_dict):
    for mon in oppOpt_dict:
        print("Opposing "+mon+": Do not use "+str(oppOpt_dict[mon]))



        
    
main()
