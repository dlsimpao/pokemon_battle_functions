#Random Password Generator

#include parameters: Symbol exlusion, capital letters, numbers, length
import random

def genPassword(num, specialChar):

    password = ""

    #makes sure valid parameters
    if num != int(num) or specialChar != bool(specialChar):
            print("GenPassword(int,specialChar = True)... Please enter the appropriate parameters.")

    #dictionaries of possible characters
    alph = {1:"a",2:"b",3:"c",4:"d",5:"e",6:"f",7:"g",8:"h",9:"i",10:"j",11:"k",12:"l",13:"m"\
            ,14:"n",15:"o",16:"p",17:"q",18:"r",19:"s",20:"t",21:"u",22:"v",23:"w",24:"x",25:"y",26:"z"}

    nums = {1:"1",2:"2",3:"3",4:"4",5:"5",6:"6",7:"7",8:"8",9:"9",10:"0"}

    sym = {1:"!",2:"@",3:"#",4:"$",5:"%",6:"^",7:"&",8:"*"}

    for i in range(num):
        charType_prob = random.random()
        if (specialChar == True and charType_prob < 1/3) or (specialChar == False and charType_prob < 1/2):
            dict_prob = random.randint(1,len(alph))
            case_prob = random.random()
            if case_prob < 1/2:
                password += alph[dict_prob]
            else:
                password += alph[dict_prob].upper()
        elif(specialChar == True and charType_prob < 2/3) or (specialChar == False and charType_prob < 1):
            dict_prob = random.randint(1,len(nums))
            password += nums[dict_prob]
        else:
            dict_prob = random.randint(1,len(sym))
            password += sym[dict_prob]
    print("This is your generated password:\t"+password)
            
            

    

        

    

    

