#Pokemon Battle Simulation Test

import PMonsterClass as pmc
import TypeMatchups as tm
import pkmnTeamGenerator as ptg

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
    optimizeParty(myPokeParty,oppPokeParty,natPokeType_dict)
    

    



#strips newline and splits at ','
def strNspl(line):
    line = line.strip("\n")
    line = line.split(",")
    return line

#opens Pokemon Database
def createTypeDict(handleStr):
    pokeType_dict = {}
    fHandle = open("PGenAll170719.csv")
    header = fHandle.readline()
    header = strNspl(header)
    for line in fHandle:
        line = strNspl(line)
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
    print("My Pokemon: "+str(myTypes_dict))
    for mon in opp_list:
        oppTypes_dict[mon] = getType(mon,type_dict)
    space()
    print("Opposing Pokemon: "+str(oppTypes_dict))

    #for each pokemon in opponents party, find their matchup effectiveness
    for mon in oppTypes_dict:
        immuneAgainst, superResistantAgainst, resistantAgainst, weakAgainst,superWeakAgainst = tm.getEffectMatch(oppTypes_dict[mon])
        effect_list = tm.capLists([immuneAgainst, superResistantAgainst, resistantAgainst, weakAgainst,superWeakAgainst])
        oppTypesMatchup[mon] = effect_list
    space()
    
    print(oppTypesMatchup)
    space()
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
                        oppList = []
                        if isinstance(myOptLineUp.get(myMon),list):
                            oppList = myOptLineUp.get(myMon)
                        else:
                            oppList.append(myOptLineUp.get(myMon))
                        #adds new info
                        if oppMon not in oppList:
                            oppList += [oppMon]
                        #adds to dictionary
                        myOptLineUp[myMon] = oppList
        for oppTypes in oppTypesMatchup[oppMon][3]: #-------------------------------needs work
            #for each pokemon in my party
            for myMon in myTypes_dict:   
                if oppTypes in myTypes_dict[myMon]:
                    if myMon not in myOptLineUp:
                        myOptLineUp[myMon] = oppMon
                    else:
                        #resets lists
                        oppList2 = []
                        if isinstance(myOptLineUp.get(myMon),list):
                            oppList2 = myOptLineUp.get(myMon)
                        else:
                            oppList2.append(myOptLineUp.get(myMon))
                        #adds new info
                        if oppMon not in oppList2:
                            oppList2 += [oppMon]
                        #adds to dictionary
                        myOptLineUp[myMon] = oppList2
    print(myOptLineUp)

def space():
    print("\n\n\n")
        
    
main()
