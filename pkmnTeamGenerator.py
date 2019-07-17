#random Pokemon party generator

import PBattleSim.py as pbsim

pokeName_list = []

fHandle = open("PGenALL170719.csv")
header = strNspl(header)
    for line in fHandle:
        line = pbsim.strNspl(line)
        pokeName_list.append(line)
print(pokeName_list)
