#P-Type Counters - generates type matchups

#def main():
    #ans1 - answer for dual type
    

    

def effectivityOf(type1,type2 = None):
    type_list = ["normal","fighting","flying","poison","ground","rock","bug","ghost","steel"\
                 "fire","water","grass","electric","psychic","ice","dragon","dark","fairy","none",None]
    dualType = False
    
    try:
        if type1 or type2 in type_list:
            type1.lower()
            if type2 != None:
                type2.lower()
                dualType = True
                
        
    except:
        print("Please enter valid types from this list:\n")
        for i in range(len(type_list)-2):
            print(type_list[i]) #we can use end = "" to remove newline character

    #dictionaries of type effectiveness
    norm_effect = {"rock":0.5, "ghost":0, "steel":0.5}
    fight_effect = {"normal":2, "flying":0.5, "poison":0.5,"rock":2,"bug":0.5,"ghost":0,"steel":2,"psychic":0.5,"ice":2,"dark":2,"fairy":0.5}
    fly_effect = {"fighting":2, "rock":0.5, "bug":2,"steel":0.5, "grass":2, "electric":0.5}
    pois_effect = {"poison":2,"ground":0.5, "rock":0.5, "ghost":0.5,"steel":0,"grass":2,"fairy":2}
    ground_effect = {"flying":0, "poison":2,"rock":2,"bug":0.5,"steel":2,"fire":2,"grass":0.5,"electric":2}
    rock_effect = {"fighting":0.5,"flying":2,"ground":0.5,"bug":2,"steel":2,"fire":2,"ice":2}
    bug_effect = {"fighting":0.5,"flying":0.5,"poison":0.5,"ghost":0.5,"steel":0.5,"fire":0.5,"grass":2,"psychic":2,"dark":2,"fairy":0.5}
    ghost_effect = {"normal":0,"ghost":2,"psychic":2,"dark":0.5}
    steel_effect = {"rock":2,"steel":0.5,"fire":0.5,"water":0.5,"electric":0.5,"ice":2,"fairy":2}
    fire_effect = {"rock":0.5,"bug":2,"steel":2,"fire":0.5,"water":0.5,"grass":2,"ice":2,"dragon":0.5}
    water_effect = {"ground":2,"rock":2,"fire":2,"water":0.5,"grass":0.5,"dragon":0.5}
    grass_effect = {"flying":0.5,"poison":0.5,"ground":2,"rock":2,"bug":0.5,"steel":0.5,"fire":0.5,"water":2,"grass":0.5,"dragon":0.5}
    elec_effect = {"flying":2,"ground":0,"water":2,"grass":0.5,"electric":0.5,"dragon":0.5}
    psych_effect = {"fighting":2,"poison":2,"steel":2,"psychic":0.5,"dark":0}
    ice_effect = {"flying":2,"ground":2,"steel":0.5,"fire":0.5,"water":0.5,"grass":2,"ice":0.5,"dragon":2}
    drgn_effect = {"steel":0.5,"dragon":2,"fairy":0}
    dark_effect = {"fighting":0.5,"ghost":2,"psychic":2,"dark":0.5,"fairy":0.5}
    fairy_effect = {"fighting":2,"poison":2,"steel":0.5,"fire":0.5,"dragon":2,"dark":2}

    

    
#matchups(23,32)
#matchups("fire","none")
#matchups("Fire","fighting")
