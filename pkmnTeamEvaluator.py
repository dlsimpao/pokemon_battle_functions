#pkmnTeamEvaluator
import pkmnTeamClass as ptc
import pkmnBattleMatchups as pbm
import pkmnTypeMatchups as tm

import pkmnData as pd
import conventionalCode as cc

#methods
#getPkmn_MoveTypes(obj)

#create a scoring system that depicts favor to win

def main():
    #dictionary of pkmn and their types
    pt_dict = pd.pkmnTypes_dict
    penguin = ptc.pkmnTeam(["Type: Null", "Jangmo-o", "Kommo-o", "Mareanie", "Shiinotic","Porygon2"])

    #generated pkmn team instance
    #penguin = ptc.pkmnTeam()
    
    #randomly generated pkmn team
    #penguin.randomizeParty(6)
    
    print("Penguin\n")
    penguin.printParty()

    
    #sets random moves for each pkmn in the party
    for mon,obj in penguin.getParty().items():
        #list of types of pkmn in the party
        types = [x.upper() for x in pt_dict[mon]]
        move_list = ptc.genPokeMoves(4,types) 
        for move in move_list:
            obj.setMove(move)
        
    #cc.space(1)
    
    myPkmn_dict = penguin.getParty()
##    for mon,obj in myPkmn_dict.items():
##        print(obj)
##        cc.space(1)
    
    cc.space(1)

    #harded-coded opponent team    
##    ostrich = ptc.pkmnTeam(["Lotad", "Croagunk", "Pikipek", "Nidoran?", "Spinda", "Articuno"])
    #opponent generated team
    ostrich = ptc.pkmnTeam()
    ostrich.randomizeParty(6)
    print("Ostrich\n")
    ostrich.printParty()

    cc.space(1)

    #creates random moves for each pkmn in the party
    oppPkmn_dict = ostrich.getParty()
    for mon,obj in oppPkmn_dict.items():
        types = [x.upper() for x in pt_dict[mon]]
        move_list = ptc.genPokeMoves(4,types)
        for move in move_list:
            obj.setMove(move)

    #prints each opposing pkmn and their movesets
##    for mon,obj in oppPkmn_dict.items():
##        print(obj)
##        cc.space(1)

    #pbm.summaryMatchup(myPkmn_dict.keys(),oppPkmn_dict.keys())

    #dictionary; key = object, values = pkmn type and move types
##    oppTypes_dict = getPkmn_MoveTypes(ostrich)
##    for obj,types in oppTypes_dict.items():
##        print(obj.getName(),types)

    #dictionary; key = object, values = dictionary w/ key = move, value = effect statements
    printTeamMovesSummary(oppPkmn_dict)
    printAdvice(myPkmn_dict,oppPkmn_dict,"attack")
    printAdvice(myPkmn_dict,oppPkmn_dict,"defense")

    printMatchupReport(evalMatchup(myPkmn_dict,oppPkmn_dict),evalMatchup(oppPkmn_dict,myPkmn_dict))

def evalMatchup(myTeam,oppTeam):
    matchup_score = 0
    for oppName,obj in oppTeam.items():
        for name,moves in getTeamMoveEvals(myTeam).items():
            for move,effect in moves.items():
                if cc.haveCommon([effect[2],pd.getPkmnTypes(oppName)]):
                    matchup_score += 1
    return matchup_score

def printMatchupReport(myScore,oppScore):
    print("Your Score:"+ str(myScore))
    print("Opponent's Score:"+ str(oppScore))
        
        

#receives team list, returns dictionary, key = name, value = types
def getTeamTypes(team_list):
    pkmnType_dict = {}
    for pkmn in team:
        pkmnType_dict[pkmn] = pd.getPkmnTypes(pkmn)
    return pkmnType_dict
                         

#receives a list of moves and evaluates it, returning a dictionary (key = move, value = list of effect matchups)

def getMoveEvals(moves_list):
    fHandle = pd.getFHandle("Moves")
    pkmnMT_dict = pd.autoDict(fHandle, ["Name","Type","Cat."],index = False)
    evalMoves_dict = {}
    for move in moves_list:
        evalMoves_dict[(pkmnMT_dict[move][1],move)] = tm.getMoveTypeEffects(pkmnMT_dict[move][0],pd.typesMatchup_dict)
    return evalMoves_dict

def compareMoveEvals(mEvals,pkmnTeam):
    goodMove_list = []
    for move,effects in mEvals.items():
        for pkmn,obj in pkmnTeam.items():
            if cc.haveCommon([mEvals[move][2],pd.getPkmnTypes(pkmn)]):
                moveAdvice = str(move)+" against "+str(pkmn)
                goodMove_list.append(moveAdvice)
    return goodMove_list

#function receives my opponent's and my pkmn dictionary for our team
#returns which moves to use against which opposing pkmn
def printAdvice(myTeam,oppTeam, advice = "attack"):
    if advice.lower() == "attack":
        for name, effect in getTeamMoveEvals(myTeam).items():
            attackGuide = compareMoveEvals(effect,oppTeam)
            for attack in attackGuide:
                print("Use "+name+"'s"+attack)
            cc.space(1)
    elif advice.lower() == "defense":
        for name, effect in getTeamMoveEvals(oppTeam).items():
            attackGuide = compareMoveEvals(effect,myTeam)
            for attack in attackGuide:
                print("Avoid opposing "+name+"'s"+attack)
            cc.space(1)

#returns pkmn dict key = name, value = effect evaluations
def getTeamMoveEvals(teamObj_dict):
    #dictionary; key = object, values = dictionary w/ key = move, value = effect statements
    pkmnEval_dict = {}
    for name,obj in teamObj_dict.items():
        pkmnEval_dict[name] = getMoveEvals(obj.getMoves())
    return pkmnEval_dict

#function takes in a dictionary; key = name, value = obj
#returns a summary report of pkmn and move type effects
def printTeamMovesSummary(teamObj_dict):
    #dictionary; key = object, values = dictionary w/ key = move, value = effect statements
    pEval_dict = getTeamMoveEvals(teamObj_dict)
        
    for name, effects in pEval_dict.items():
        print(name + str(cc.retNonBlanks(pd.getPkmnTypes(name))))
        printMoveEvals(effects)
        cc.space(1)
        

def printMoveEvals(mEvals):
    print("{:<40}{:<20}{:<65}{:<45}".format("Category || Moves","has no effect","not very effective","super effective"))
    for key in mEvals:
        print("{:<40}{:<20}{:<65}{:<45}".format(str(key),str(mEvals[key][0]),str(mEvals[key][1]),str(mEvals[key][2])))
 

main()
    
