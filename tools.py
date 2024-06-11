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
    
def sort_list(entry_list:list,sorting_index:int,ascending=True): 
    if ascending: # az kochik be bozorg
        for round in range(0, len(entry_list)-1):
            for index in range(0, len(entry_list)-1):
                if entry_list[index][sorting_index] > entry_list[index+1][sorting_index]:
                    entry_list[index][sorting_index], entry_list[index+1][sorting_index] = entry_list[index+1][sorting_index], entry_list[index][sorting_index]
    else: # az bozorg be kochik
        for round in range(0, len(entry_list)-1):
            for index in range(0, len(entry_list)-1):
                if entry_list[index][sorting_index] < entry_list[index+1][sorting_index]:
                    entry_list[index][sorting_index], entry_list[index+1][sorting_index] = entry_list[index+1][sorting_index], entry_list[index][sorting_index]

    return entry_list

def get_input(type:int, prompt:str, valid_options:list=None,return_none_on: str=None):
    """
    type 1:
        Gets int

    type 2:
        Gets float

    type 3:
        Gets str

    type 4:
        get str without numbers
    """
    if type == 1:  # get int
        while True:
            value = input(prompt).strip().lower()
            if value == return_none_on:
                return None
            try:
                value = int(value)
                if valid_options:
                    if value in valid_options:
                        return value
                    else:
                        print(f"Please enter one of the following: {valid_options}")
                else:
                    return value
            except ValueError:
                print("Invalid input. Please enter a valid integer.")
    
    elif type == 2: # get float
        while True:
            value = input(prompt).strip().lower()
            if value == return_none_on:
                return None
            try:
                value = float(value)
                if valid_options:
                    if value in valid_options:
                        return value
                    else:
                        print(f"Please enter one of the following: {valid_options}")
                else:
                    return value
            except ValueError:
                print("Invalid input. Please enter a valid float.")

    if type == 3: # get str input
        while True:
            value = input(prompt).strip().lower()
            if value == return_none_on:
                return None
            elif valid_options:
                if value in valid_options:
                    return value
                else:
                    print(f"Please enter one of the following: {valid_options}")
            else:
                return value
            
    if type == 4:  # get str without numbers
        while True:
            value = input(prompt).strip()
            if value == return_none_on:
                return None
            if any(char.isdigit() for char in value):
                print("Invalid input. Please enter a string without numbers.")
            else:
                if valid_options:
                    if value in valid_options:
                        return value
                    else:
                        print(f"Please enter one of the following: {valid_options}")
                else:
                    return value

            
def is_str_contains_int(entry_str):
    for char in list(entry_str):
        if char.isdigit() == True:
            return True