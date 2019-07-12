#damage calc

import random
#def getTypeMatchup() #get from Proj 2

#gen - 1,2,3,4,5,6,7,8,9
#myMoveType - types
#targets - 1,2
#earnedBadgeType - T/F

#A level 75 glaceon, no burn, no items, attack stat of 123, - uses Ice Fang of power 65. STAB 
#against Garchomp with Def 163 in GEN 6. No crit. typeMatchup has a double weakness, typeMatch = 4

#damage should be around 168,196 depending on luck

#Gen6, ice, 1, False, normal, 1, 1, True, 4, no, None
#level 75, power of 65, attack of 123, 163, mod 

def main():
    mod, modInt = getModifier(6,"ice",1,False,"normal",50,1,True, 4, False, None)
    damage = showDamageOutput(75, 65, 123, 163, mod)
    damageInt = [showDamageOutput(75,65,123,163,x) for x in modInt]
    print("On average, you deal ",int(damage),"damage.\n"\
          "Depending on luck, your damage varies from"+str([int(x) for x in damageInt]))
    

def getModifier(gen, myMoveType, targets, earnedBadgeType, weather, speed, crit_other, STAB, typeMatch, burn, other):
    mod_list = []

    #targets
    if targets > 1 and gen == 3:
        mod_list.append(0.5)
    elif targets > 1:
        mod_list.append(0.75)
    else:
        mod_list.append(1)

    #badge type and myMoveType
    if earnedBadgeType:
        mod_list.append(1.25)
        
    #weather
    weatherMod = effectWithWeather(myMoveType, weather)
    mod_list.append(weatherMod)

    #critical
    probCrit = prob_getCrit(speed, crit_other)
    if getCrit(probCrit):
        if gen > 1 and gen < 6:
            mod_list.append(2)
        else:
            mod_list.append(1.5)

    #STAB
    if STAB:
        mod_list.append(1.5)

    #typematch
        mod_list.append(typeMatch)

    #user burned
    if burn and move_effect == "physical" and gen > 3:
        mod_list.append(0.5)

    #other items
    if other != None:
        mod_list.append(other)

    #modifier before random
    modifier = multiplyInList(mod_list)

    #random
    if gen > 3:
        #randval = random.uniform(0.85,1) #uncomment for variance
        randval = 0.925 #average value
        modifier_confInt = [modifier*x for x in [0.85,1]]#supplement to random: confidence interval
    else:
        randval = random.randint(217,255)
        randval = randval/255
        modifier_confInt = [modifier * x for x in [217/255, 1]]#supplement to random: confidence interval
        
    modifier = modifier * randval
    
    return modifier, modifier_confInt
        

def prob_getCrit(speed, other):

    #moves that influence speed
    speed = int(speed)
    if speed % 2 != 0:
        speed -= 1
        
    T = (speed*other) / 2
    T = min(255,T)
    #print(T)
    P = T / 256

    return P

def getCrit(prob):
    crit = False
    val = random.random()
    if val < prob:
        crit = True
    return crit
    

def effectWithWeather(myMoveType, weather):
    effect = 1
    if weather.lower() == "harsh sunlight" and myMoveType.lower() == "water":
        effect = 0.5
    elif weather.lower() == "harsh sunlight" and myMoveType.lower() == "fire":
        effect = 1.5
    elif weather.lower() == "rain" and myMoveType.lower() == "water":
        effect = 1.5
    elif weather.lower() == "rain" and myMoveType.lower() == "fire":
        effect = 0.5
    else:
        effect = 1
    return effect
        


#multiplies all elements in a list    
def multiplyInList(alist):
    if alist == []:
        return 1
    else:
        return alist[-1]*multiplyInList(alist[:len(alist)-1])

def showDamageOutput(level, power, myAttack,oppDefense,modifier):
    dmg1 = (((2*level)/5)+2)*power*myAttack*(1/oppDefense)
    dmg = ((dmg1/50)+2)*modifier
    return dmg

main()

