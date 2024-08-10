# password Generator 
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


Set_User_Setting()
print(user_setting)












