#Pokemon Battle Simulation Test

#pkmnData has pkmnType_dict and pkmnMoveType_dict dictionaries
import pkmnData as pd
import conventionalCode as cc #
import pkmnTeamGenerator as ptg #creates random team

import pkmnClass as pmc #
import pkmnTypeMatchups as tm #



def main():
    #national Pokemon Dict
    type_dict = pd.pkmnTypes_dict
    

    #max six Pokemon in a party
    num = 6
    myPokeParty = ptg.genPokeTeam(num)
    oppPokeParty = ptg.genPokeTeam(num)

    #moveList = ptg.genPokeMoves(4)
    #print(moveList)
    #myPokeParty = createTeam(["Hitmonlee","Primeape","Articuno","Elgyem","Rowlet","Gastrodon"])
    #oppPokeParty = createTeam(["Weavile","Sneasel","Krabby","Starly","Leafeon","Basculin"])

    #stores the optimal party setup, assuming no switches and advantage based solely on type

    #Mine
    myOptParty = optimizeParty(myPokeParty,oppPokeParty)
    oppStrong = getStrongOpp(myOptParty, oppPokeParty)


    #Opp
    oppOptParty = optimizeParty(oppPokeParty, myPokeParty)
    myStrong = getStrongOpp(oppOptParty, myPokeParty)


##    printParty(myPokeParty,"Penguin's Team")
##    cc.space(2)
##    printParty(oppPokeParty,"Evil Ostrich's Team")
##    cc.space(2)
##    printFavorMatch(myOptParty, myStrong)
##    cc.space(2)
##    printAvoidMatch(oppOptParty, oppStrong)

    

#creates roster of proper names
def createTeam(l):
    l = [x.title() for x in l]
    return l

#creates a sub type dict specifically for the team
def createTeamTypesDict(party):
    ret_dict = {}
    for mon in party:
        ret_dict[mon] = pd.pkmnTypes_dict[mon]
    return ret_dict

#create custom dictionary for team
def createTeamMatchupDict(party_dict):
    ret_dict = {}
    for mon in party_dict:
            ret_dict[mon] = tm.getEffectMatch(party_dict[mon])
    return ret_dict

#Given I know opponent's lineup, I optimize my party's order (based on type, not move types)
def optimizeParty(myRoster,oppRoster):
    myOptTeam = {}
    
    myTypes_dict = createTeamTypesDict(myRoster)
    oppTypes_dict = createTeamTypesDict(oppRoster)

    #key = pkmn, value = tuples of (immuneAgainst, superResistantAgainst, resistantAgainst, weakAgainst,superWeakAgainst)
    myMatchup_dict = createTeamMatchupDict(myTypes_dict)
    oppMatchup_dict = createTeamMatchupDict(oppTypes_dict)

    for mon in myTypes_dict:
        for opp in oppMatchup_dict:
            if cc.haveCommon([[*myTypes_dict[mon]],*oppMatchup_dict[opp][3:]]):
                if mon not in myOptTeam:
                    myOptTeam[mon] = opp
                elif opp not in myOptTeam[mon]:
                    oldOpp = myOptTeam.get(mon)
                    newOpp = cc.cascadeTuples((oldOpp,opp))
                    myOptTeam[mon] = newOpp
    return myOptTeam

#prints party
def printParty(party,header = ""):
    if header != "":
        print(header)
    types_dict = createTeamTypesDict(party)
    for mon in types_dict:
        if types_dict[mon][1] == "":
            print(mon+": "+str(types_dict[mon][0]))
        else:
            print(mon+": "+str(types_dict[mon][0]+" "+str(types_dict[mon][1])))

#NEXT: get and print functions

#identifies which opposing Pokemon will go evenly or better than mine
#given my optimal lineup dictionary and opponents' list
def getStrongOpp(myOpt_dict, oppList):
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

def printStrongOpp(opt_dict, oppList):
    ret_list = getStrongOpp(opt_dict, oppList)
    for mon in ret_list:
        print(mon)

#prints desired matchups
def printFavorMatch(myOpt_dict, strongPoke = ""):
    for mon,opp in myOpt_dict.items():
        print("My "+mon+": Use against "+str(opp))
    print("Opposing team has no type counter for "+str(strongPoke))


#prints unwanted matchups
def printAvoidMatch(oppOpt_dict, strongPoke = ""):
    for mon,opp in oppOpt_dict.items():
        print("Opposing "+mon+": Do not use " +str(opp))
    print("My team has no type counter for "+str(strongPoke))

def summaryMatchup(myParty,oppParty):
    myOptParty = optimizeParty(myParty,oppParty)
    oppStrong = getStrongOpp(myOptParty,oppParty)
    
    printFavorMatch(myOptParty, oppStrong)

    cc.space(1)
    
    oppOptParty = optimizeParty(oppParty,myParty)
    myStrong = getStrongOpp(oppOptParty, myParty)

    printAvoidMatch(oppOptParty,myStrong)


        
    
main()
