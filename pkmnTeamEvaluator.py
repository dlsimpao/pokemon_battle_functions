#pkmnTeamEvaluator
import pkmnTeamGenerator as ptg
import pkmnBattleMatchups as pbm
import pkmnData as pd
import conventionalCode as cc
import pkmnTypeMatchups as tm

def main():
    pt_dict = pd.pkmnTypes_dict
    penguin = ptg.pkmnTeam(["Blitzle", "Sudowoodo", "Wormadam (T)", "Mareanie", "Shiinotic","Porygon2"])
##    penguin.randomizeParty(6)
    print("Penguin\n")
    penguin.printParty()

    #figure out how to generate random pokemon of the Pokemon's type and set it as their moveset
    for mon,obj in penguin.getParty().items():
        types = [x.upper() for x in pt_dict[mon]]
        move_list = ptg.genPokeMoves(4,types, cat = ["Physical","Special"]) 
        print(types)
        for move in move_list:
            obj.setMove(mon)
        
    cc.space(1)
    myPkmn_dict = penguin.getParty()
    for mon,obj in myPkmn_dict.items():
        print(obj)
    
    cc.space(1)
    
    ostrich = ptg.pkmnTeam(["Lotad", "Croagunk", "Pikipek", "Nidoran?", "Spinda", "Articuno"])
##    ostrich.randomizeParty(6)
    print("Ostrich\n")
    ostrich.printParty()


main()
    
