from os import system
from colorama import Fore

def ClearTerminal():
    system('cls')

def Wait():
    input("Press Enter to Continue!!!")

def ColoredNotification(text:str, color:str,) -> str:
    """
    :Arguments:
    :text - Enter whatever you want to write
    :color - you can choose your text color between 3 colors "red","green","cyan"

    :Return:
    :It returens your text with your requested color
    :⚠️ Dont forget to print it or use it in input func ⚠️
    """
    if color == "red":
        return (Fore.RED + text + Fore.WHITE)
    elif color == "green":
        return (Fore.GREEN + text + Fore.WHITE)
    elif color == "cyan":
        return (Fore.CYAN + text + Fore.WHITE)
    
def TextStructure(text, desired_width):
    remaining_space = desired_width - len(text)
    if remaining_space % 2 == 0:
        spaces_width = int(remaining_space / 2)
        return (spaces_width * ' ' + text + spaces_width * ' ')
    else:
        spaces_width = int(remaining_space // 2)
        return (spaces_width * ' ' + text + (spaces_width + 1) * ' ')
    
def get_input(type:int, prompt:str, valid_options:list=None,return_none_on: str=None):
    """
    type 1:
        Gets int

    type 2:
        Gets float

    type 3:
        Gets str
    """
    if type == 1: # get int
        while True:
            while True:
                value = int(input(prompt).strip().lower())
                if value == return_none_on:
                    return None
                elif valid_options:
                    if value in valid_options:
                        return value
                    else:
                        print(f"Please enter one of the following: {', '.join(valid_options)}")
                else:
                    return value
    
    elif type == 2: # get float
        while True:
            value = float(input(prompt).strip().lower())
            if value == return_none_on:
                return None
            elif valid_options:
                if value in valid_options:
                    return value
                else:
                    print(f"Please enter one of the following: {', '.join(valid_options)}")
            else:
                return value

    if type == 3: # get str input
        while True:
            value = input(prompt).strip().lower()
            if value == return_none_on:
                return None
            elif valid_options:
                if value in valid_options:
                    return value
                else:
                    print(f"Please enter one of the following: {', '.join(valid_options)}")
            else:
                return value