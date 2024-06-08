from tools import *
from colorama import Fore, Back, Style
from users import Users
import getpass
from datetime import datetime
from item import Item

class Main:
    selectedUser = Users("","","","","","","","","","","")
    users = []

######################################## ONLINE SHOP ########################################
############################# Main Menu Terminal Design Sketch ##############################
### Cart | Sign In | Sign UP | Categories | Search | Customer Service | Gift Cards | Sell ###
### ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾ ###
### 1. Suggestion | 2.Suggeestion | .          .           .          .           .       ###
### Recently Visited                                                                      ###
#############################################################################################

def ShowMainMenu():
    UsersUpdate()
    with open("DB\\theLatestLoginUserId.txt","r") as file:
        lastLoginId = file.read()
        if lastLoginId != "":
            SearchUser("","",lastLoginId)
        file.close()
    if Main.selectedUser.username == "":
        print(Fore.RED + "You are not logged in!" + Fore.WHITE)
        print(Fore.GREEN + "Cart(0) | Sign In | Sign UP | Categories | Search | Customer Service | Gift Cards | Sell" + Fore.WHITE)
    else:
        # When Admins Enter
        if Main.selectedUser.role == "2":
            print(ColoredNotification(Main.selectedUser.fname + " " + Main.selectedUser.lname,"cyan"))
            print(ColoredNotification("Admin Panel: Add Item | Show Items","red"))
            print(ColoredNotification("Cart(0) | Sign Out | Categories | Search | Customer Service | Gift Cards | Sell  ","green"))

        # When Moderators Enter
        elif Main.selectedUser.role == "1":
            print(ColoredNotification("Moderator","cyan"))
            print(ColoredNotification(Main.selectedUser.fname + " " + Main.selectedUser.lname,"cyan"))
            print(ColoredNotification("Cart(0) | Sign Out | Categories | Search | Customer Service | Gift Cards | Sell","green"))

        # When Normal Users Enter
        else:
            print(ColoredNotification(Main.selectedUser.fname + " " + Main.selectedUser.lname,"cyan"))
            print(ColoredNotification("Cart(0) | Sign Out | Categories | Search | Customer Service | Gift Cards | Sell","green"))

def SearchUser(username, password, id): 
    for user in Main.users:
        if (user[1] == username and user[2] == password) or user[0] == id:
            Main.selectedUser = Users(user[0], user[1], user[2], user[3], user[4], user[5],user[6],user[7],user[8],user[9],user[10])
            # Write in theLatestLoginUserId the Latest user logged in
            with open("DB\\theLatestLoginUserId.txt","w") as file:
                file.write(user[0])
                file.close()

def Cart():
    flag = True
    while flag:
        pass

def UsersUpdate():
    file = open("DB\\users.txt","r")
    Main.users = file.read().split("/")
    Main.users.pop(-1)
    file.close()
    for index, user in enumerate(Main.users):
        Main.users[index] = user.split(",")

def LastUserID():
    UsersUpdate()
    if Main.users == []:
        return 1
    lastUserId = int(Main.users[-1][0])
    return lastUserId + 1

def getEntry(question):
    flag = True
    while flag:
        ClearTerminal()
        answer = input(question)
        if ',' in answer or '/' in answer:
            print(Fore.RED + "You can't use '/' or ','" + Fore.WHITE)
            Wait()
        else: 
            break
        
    return answer

#############################################################################################################
################################################## USERS ####################################################
## id, username, password, fname, lname, phone, isPhoneVerifyed, nationalId, dateOfBirth, role, last login ##
#############################################################################################################
#############################################################################################################

def SignUpMenu():    
    ClearTerminal()
    print(Fore.GREEN + "Sign Up")
    print(Fore.RED + "DON'T USE '/' or ','" + Fore.WHITE )
    userId = LastUserID()
    username = getEntry("Username: ")
    password = getEntry("Password: ")
    fname = getEntry("First Name: ")
    lname = getEntry("Last Name: ")
    phone = getEntry("Phone Number: ")
    # TODO: IF username exists
    with open("DB\\users.txt","a") as file:
        file.write(f"{userId},{username},{password},{fname},{lname},{phone},,,,0,{datetime.now()}/")
        file.close()
    Main.selectedUser = Users(userId, username, password, fname, lname, phone,"","","","0",datetime.now())
    with open("DB\\theLatestLoginUserId.txt","w") as file:
        file.write(str(userId))
        file.close()

def SignInMenu():
    ClearTerminal()
    UsersUpdate()
    print(Fore.GREEN + "Sign In" + Fore.WHITE )
    username = input("Username: ")
    password = getpass.getpass("Password: ")
    SearchUser(username,password,"")

########################################################################### ITEM FORMAT ############################################################################
### id | name | count | price | rating | Seller Shop | category | Detail | Features [Sub Feutures []] | Created Date | Created by | IsDiscounted | Discount Date ###
####################################################################################################################################################################
def AddItemMenu():
    ClearTerminal()
    if Main.selectedUser.role == "2":
        flag = True
        while flag:
            name = getEntry("item Name: ")
            count = getEntry("item Count: ")
            price = getEntry("item Price: ")
            rating = 0
            sellerShop = getEntry("What is the Seller Shop Name: ") #TODO it must be deleted from this menu and equalls to Parsa Shop
            category = getEntry("item Category: ")
            detail = getEntry("item Detail: ")
            features = getEntry("item Features: ")
            createdDate = datetime.now()
            createdBy = Main.selectedUser.username
            isDiscounted = "0"
            discountDate = ""
            selectedItem = Item(Item.getId(), name,count,price,rating,sellerShop,category,detail,features,createdDate,createdBy,isDiscounted,discountDate)
            with open("DB\\item.txt", "w") as file:
                file.write(f"{1},{name},{count},{price},{rating},{sellerShop},{category},{detail},{features},{createdDate},{createdby},{isDiscounted},{discountDate}/")
                file.close()

            print(ColoredNotification("The item Added Successfuley", "green"))
            # Do admin wants to add more item?
            answer = input("Anything to Continue\n0 to EXIT\n> ")
            if answer == "0":
                flag = False
                break

def ShowItems():
    if Main.selectedUser.role == "2": # if admin enters
        with open("DB\\item.txt", "r") as file:
            fileText = file.read()
            fileText = fileText.split("/")
            fileText.pop(-1)
            for item in fileText:
                item = item.split(",")
            for item in fileText:
                print(item)
            Wait()
            file.close()

def MainMenu():
    mainMenuFlag = True
    while mainMenuFlag:
        ClearTerminal()
        ShowMainMenu()
        answer = input(Fore.CYAN + "> ").lower()
        if answer == "cart":
            Cart()
        elif answer == "sign up":
            SignUpMenu()
        elif answer == "sign in":
            SignInMenu()
        elif answer == "sign out":
            if Main.selectedUser.id == "":
                print(Fore.RED+"You are not signed in!!!"+Fore.WHITE)
                Wait()
            else:
                with open("DB\\theLatestLoginUserId.txt","w") as file:
                    file.write("")
                    file.close()
                Main.selectedUser = Users("","","","","","","","","","","")
                print(Fore.GREEN+"You are signed out Successfully!!!"+Fore.WHITE)
                Wait()
        elif answer == "add item":
            AddItemMenu()
        elif answer == "show item":
            ShowItems()
        elif answer == "!help":
            pass
        else:
            print("Do you need a help? use this command '!help'")
            Wait()


###############################
## Main Program Starts HERE! ##
###############################
MainMenu()