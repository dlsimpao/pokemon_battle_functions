#Pokemon party evaluator
#evaluates the party based 
import conventionalCode as cc
import pkmnData as pd
import pkmnTeamGenerator as ptg
import TypeMatchups as tm


#include physical, status effects
def main():
    fHandle = pd.getFHandle("Moves")
    #print(pd.getHeader(fHandle))
    #creates a dictionary, name as key, type and cat. as values
    pkmnMoveType_dict = pd.autoDict(fHandle, ["Name","Type","Cat."],index = False)
    types_dict = pd.getTypes_dict()

##    for key in pkmnMoveType_dict:
##        print(pkmnMoveType_dict[key])
    #moves = ptg.genPokeMoves(4,["normal","fire"],["Physical","Special"])
    #moves = ptg.genPokeMoves(4,["normal","fire"],["Status"])
    moves = ptg.genPokeMoves(4,["water","fire"],["Physical"])
    moveEvals = getMoveEvals(moves,pkmnMoveType_dict,types_dict)
    printMoveEvals(moveEvals)
    
#receives a list of moves and evaluates it, returning a dictionary (key = move, value = list of effect matchups)
        
def getMoveEvals(moves_list, pkmnMT_dict,types_dict):
    evalMoves_dict = {}
    for move in moves_list:
        evalMoves_dict[(pkmnMT_dict[move][1],move)] = tm.getMoveTypeEffects(pkmnMT_dict[move][0],types_dict)
    return evalMoves_dict


def printMoveEvals(mEvals):
    print("{:<45}{:<45}{:<45}{:<45}".format("Category || Moves","has no effect","not very effective","super effective"))
    for key in mEvals:
        print("{:<45}{:<45}{:<45}{:<45}".format(str(key),str(mEvals[key][0]),str(mEvals[key][1]),str(mEvals[key][2])))
        

main()
