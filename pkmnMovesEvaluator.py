#Pokemon Moves Evaluator
#evaluates the party based 


import random
import PMonsterClass as pmc
import conventionalCode as cc

import conventionalCode as cc
import pkmnData as pd
import pkmnTeamGenerator as ptg
import TypeMatchups as tm

def main():
    fHandle = pd.getFHandle("Moves")
    pkmnMoveType_dict = pd.autoDict(fHandle, ["Name","Type"],index = False)
    types_dict = pd.getTypes_dict()

##    for key in pkmnMoveType_dict:
##        print(pkmnMoveType_dict[key])
    moves = ptg.genPokeMoves(4)
    moveEvals = getMoveEvals(moves,pkmnMoveType_dict,types_dict)
    for key in moveEvals:
        print("{:<20}{:<40}{:<40}{:<40}".format(key,str(moveEvals[key][0]),str(moveEvals[key][1]),str(moveEvals[key][2])))
#receives a list of moves and evaluates it, returning a dictionary (key = move, value = list of effect matchups)
        
def getMoveEvals(moves_list, pkmnMT_dict,types_dict):
    evalMoves_dict = {}
    for move in moves_list:
        evalMoves_dict[move] = tm.getMoveTypeEffects(pkmnMT_dict[move],types_dict)
    return evalMoves_dict

main()

