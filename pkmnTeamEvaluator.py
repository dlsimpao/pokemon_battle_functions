#pkmnTeamEvaluator
import pkmnTeamClass as ptc
import pkmnBattleMatchups as pbm
import pkmnData as pd
import conventionalCode as cc
import pkmnTypeMatchups as tm

#create a scoring system that depicts favor to win

def main():
    pt_dict = pd.pkmnTypes_dict
    penguin = ptc.pkmnTeam(["Type: Null", "Jangmo-o", "Kommo-o", "Mareanie", "Shiinotic","Porygon2"])
    #penguin = ptc.pkmnTeam()
    #penguin.randomizeParty(6)
##    print("Penguin\n")
    penguin.printParty()

    
    #sets random moves for each pkmn in the party
    for mon,obj in penguin.getParty().items():
        types = [x.upper() for x in pt_dict[mon]]
        move_list = ptc.genPokeMoves(4) 
        for move in move_list:
            obj.setMove(move)
        
    #cc.space(1)
    
    myPkmn_dict = penguin.getParty()
##    for mon,obj in myPkmn_dict.items():
##        print(obj)
##        cc.space(1)
    
    #cc.space(1)
    
##    ostrich = ptc.pkmnTeam(["Lotad", "Croagunk", "Pikipek", "Nidoran?", "Spinda", "Articuno"])
    ostrich = ptc.pkmnTeam()
    ostrich.randomizeParty(6)
##    print("Ostrich\n")
##    ostrich.printParty()

    cc.space(1)

    oppPkmn_dict = ostrich.getParty()
    for mon,obj in oppPkmn_dict.items():
        types = [x.upper() for x in pt_dict[mon]]
        move_list = ptc.genPokeMoves(4)
        for move in move_list:
            #print(move)
            obj.setMove(move)
            
    oppPkmn_dict = ostrich.getParty()
    for mon,obj in oppPkmn_dict.items():
        print(obj)
        cc.space(1)

    #pbm.summaryMatchup(myPkmn_dict.keys(),oppPkmn_dict.keys())

    #dictionary; key = object, values = pkmn type and move types
    oppTypes_dict = getPkmn_MoveTypes(ostrich)
    for obj in oppTypes_dict:
        print(obj.getName())



    
#receives pkmn object, returns dictionary with pkmn type and move types
def getPkmn_MoveTypes(pkmnTeam_obj):
    pkmn_dict = pkmnTeam_obj.getParty()
    retDict = {}
        
    for name, obj in pkmn_dict.items():
        moveList = obj.getMoves()
        moveTypeList = []
        for move in moveList:
            moveTypeList.append(pd.getPkmnMoveType(move))
            
        typeList = [pd.getPkmnTypes(name), moveTypeList]
        typeList = cc.removeCommon(cc.cascadeLists(typeList))
        retDict[obj] = typeList
    return retDict

main()
    
