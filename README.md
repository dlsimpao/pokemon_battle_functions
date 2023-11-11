# pokemon_battle_functions

Tasks
- [ ] update conventionCode to miscCode
- [ ] include links for data sources
- [ ] ability module
- [ ] evolution chains 
- [ ] locations? sprites?
- [ ] items

Data | Description
----|----
PGen1.csv | data for gen 1
PGenAll170719.xlxs | data for all gen up until 7
PokeAttackdex.csv | data for all attacks
PokeAttackdex.xlsx | data for all attacks
AllPkmnGen1-7.csv | data for all gen

Modules | Description
----|----
conventionalCode.py | code for miscellaneous use  
pkmnBattleMatchups.py | creates a matchup report based on my team's and opposing team's types  
pkmnClass.py | class for pkmn object
pkmnDamageCalc.py | uses given damage formula to calculate total damage output
pkmnData.py | accesses the data, main link of other modules to the data
pkmnGen1Data_test.py | test
pkmnTeamClass.py | class for pkmn team object
pkmnTeamEvaluator.py | given two teams, evaluates which fares better in battle
pkmnTypeMatchups.py  | given a type, reports its effectiveness against other types
