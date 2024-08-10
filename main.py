# password Generator 
import string
import random
from colorama import Fore

user_setting = {"is_upper" :True,
                "is_lower":True,
                "size":8,
                "is_symbol":True,
                "is_number":True,
                "is_space":False
}
def get_true_false_input(title:str):
    while 1:
        user_input = int(input(Fore.BLUE+title+ Fore.WHITE))
        if user_input==1:
            return True
        elif user_input==0:
            return False
        else:
            print("Your input is unvalid please Enter valid input")

def Set_User_Setting():
    print("Genarator Setting :",user_setting)
    user_setting["is_upper"] = get_true_false_input("Dose Password have Upper Alphabet (Enter 0 for false or 1 for true) :")
    user_setting["is_lower"] = get_true_false_input("Dose Password have Lower Alphabet (Enter 0 for false or 1 for true) :")
    user_setting["is_symbol"] = get_true_false_input("Dose Password have Symbols (Enter 0 for false or 1 for true) :")
    user_setting["is_number"] = get_true_false_input("Dose Password have Number Alphabet (Enter 0 for false or 1 for true) :")
    user_setting["is_space"] = get_true_false_input("Dose Password have Space Alphabet (Enter 0 for false or 1 for true) :"+ Fore.WHITE)
    user_setting["size"] = int(input(Fore.BLUE+"Enter your Password size: "+ Fore.WHITE))

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
    if user_setting["is_lower"]: res.append(chose_random_lowercase) 
    if user_setting["is_upper"]:res.append(chose_random_uppercase)
    if user_setting["is_number"]:res.append(chose_random_numbercase)
    if user_setting["is_symbol"]:res.append(chose_random_symbolcase)
    if user_setting["is_space"]:res.append(return_space)
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
    print(Fore.CYAN+"Welcome to password Genrator!"+Fore.GREEN)


def main():
    welcome_page()
    Set_User_Setting()
    while 1:
        print(Genaratrat_password())
        run_again = input("Do you want anouther password ? (Yes = y, No = n) :")
        if run_again == 'y':
            continue;
        break;

main()
