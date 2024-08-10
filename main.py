# password Generator 
import string
import random
from colorama import Fore
import os

user_setting = {"is_upper" :True,
                "is_lower":True,
                "size":8,
                "is_symbol":True,
                "is_number":True,
                "is_space":False
}
def get_true_false_input(title:str):
    while 1:
        user_input = input(Fore.BLUE+title+ Fore.WHITE)
        if user_input=='1':
            return True
        elif user_input=='0':
            return False
        else:
            print("Your input is unvalid please Enter valid input")
def get_user_size():
    while 1:
        user_input = str(input(Fore.BLUE+"Enter your Password size: "+ Fore.WHITE))
        if user_input.isdigit():
            return int(user_input)
        else:
            print("Your input is unvalid please Enter valid input")

def Set_User_Setting():
    print("Genarator Setting :",user_setting)
    user_setting["is_upper"] = get_true_false_input("Dose Password have Upper Alphabet "
                                                    "(Enter 0 for false or 1 for true) :")
    user_setting["is_lower"] = get_true_false_input("Dose Password have Lower Alphabet "
                                                    "(Enter 0 for false or 1 for true) :")
    user_setting["is_symbol"] = get_true_false_input("Dose Password have Symbols "
                                                     "(Enter 0 for false or 1 for true) :")
    user_setting["is_number"] = get_true_false_input("Dose Password have Number Alphabet"
                                                     " (Enter 0 for false or 1 for true) :")
    user_setting["is_space"] = get_true_false_input("Dose Password have Space Alphabet "
                                                    "(Enter 0 for false or 1 for true) :"+ Fore.WHITE)
    user_setting["size"] = get_user_size()
def chose_random_uppercase():
    return random.choice(list(string.ascii_uppercase))


def chose_random_lowercase():
    return random.choice(list(string.ascii_lowercase))

def chose_random_numbercase():
    num_list=[0,1,2,3,4,5,6,7,8,9]
    return random.choice(num_list)
def return_space():
    return" "
def chose_random_symbolcase():
    symbol_list =[]
    for i in range(58,65):
        symbol_list.append(chr(i))
    for i in range(33,48):
        symbol_list.append(chr(i))
    for i in range(91,97):
        symbol_list.append(chr(i))
    for i in range(123,127):
        symbol_list.append(chr(i))
    return random.choice(symbol_list)
def set_availble_case():
    res= []
    zip_with_optoin={
        "is_lower":chose_random_lowercase,
        "is_upper" : chose_random_uppercase,
        "is_number" : chose_random_numbercase,
        "is_symbol":chose_random_symbolcase,
        "is_space":return_space
    }
    for option,key in user_setting.items():
        
        if type(key)==int:
            continue
        elif key==True:
            res.append(zip_with_optoin[option])
    return res
def Genarate_rand_node():
    available_case=set_availble_case()
    return random.choice(available_case)()

def Genaratrat_password():
    genrated_pass = ""
    for num in range(int(user_setting["size"])):
        genrated_pass+= str(Genarate_rand_node())
    return genrated_pass
def welcome_page():
    os.system("cls")
    print(Fore.CYAN+"Welcome to password Genrator!"+Fore.GREEN)
    

def main():
    welcome_page()
    Set_User_Setting()
    print('-'*20)
    while 1:
        print(f"Genrated password :"+Fore.CYAN +f"{Genaratrat_password()}" )
        print(Fore.WHITE,end="")
        run_again = input("Do you want anouther password ? (Yes = y, No = n) :")
        if run_again == 'y':
            continue
        break

main()
