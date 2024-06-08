from tools import *
from item import Item
from users import Users


######################################## ONLINE SHOP ########################################
############################# OnlineShop Menu Terminal Design Sketch ##############################
### Cart | Sign In | Sign UP | Categories | Search | Customer Service | Gift Cards | Sell ###
### ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾ ###
### 1. Suggestion | 2.Suggeestion | .          .           .          .           .       ###
### Recently Visited                                                                      ###
#############################################################################################

class OnlineShop:
    selectedUser = Users("","","","","","","","","","","","","")

def ShowMainMenu():
    Users.UsersUpdate()
    with open("DB\\theLatestLoginUserId.txt","r") as file:
        lastLoginId = file.read()
        if lastLoginId != "":
            Users.SearchUser("","",lastLoginId)
        file.close()
    if OnlineShop.selectedUser.username == "":
        print(Fore.RED + "You are not logged in!" + Fore.WHITE)
        print(Fore.GREEN + "Cart(0) | Sign In | Sign UP | Categories | Search | Customer Service | Gift Cards | Sell" + Fore.WHITE)
    else:
        # When Admins Enter
        if OnlineShop.selectedUser.role == "2":
            print(ColoredNotification(OnlineShop.selectedUser.fname + " " + OnlineShop.selectedUser.lname,"cyan"))
            print(ColoredNotification("Admin Panel: Add Item | Show Items","red"))
            print(ColoredNotification("Cart(0) | Sign Out | Categories | Search | Customer Service | Gift Cards | Sell  ","green"))

        # When Moderators Enter
        elif OnlineShop.selectedUser.role == "1":
            print(ColoredNotification("Moderator","cyan"))
            print(ColoredNotification(OnlineShop.selectedUser.fname + " " + OnlineShop.selectedUser.lname,"cyan"))
            print(ColoredNotification("Cart(0) | Sign Out | Categories | Search | Customer Service | Gift Cards | Sell","green"))

        # When Normal Users Enter
        else:
            print(ColoredNotification(OnlineShop.selectedUser.fname + " " + OnlineShop.selectedUser.lname,"cyan"))
            print(ColoredNotification("Cart(0) | Sign Out | Categories | Search | Customer Service | Gift Cards | Sell","green"))

def MainMenu():
    mainMenuFlag = True
    while mainMenuFlag:
        ClearTerminal()
        ShowMainMenu()
        answer = input(Fore.CYAN + "> ").lower()
        if answer == "cart":
            Cart()
        elif answer == "sign up":
            Users.SignUpMenu()
        elif answer == "sign in":
            Users.SignInMenu()
        elif answer == "sign out":
            if OnlineShop.selectedUser.id == "":
                print(Fore.RED+"You are not signed in!!!"+Fore.WHITE)
                Wait()
            else:
                with open("DB\\theLatestLoginUserId.txt","w") as file:
                    file.write("")
                    file.close()
                OnlineShop.selectedUser = Users("","","","","","","","","","","")
                print(Fore.GREEN+"You are signed out Successfully!!!"+Fore.WHITE)
                Wait()
        elif answer == "add item":
            Item.AddItemMenu()
        elif answer == "show item":
            Item.ShowItems()
        elif answer == "!help":
            pass
        else:
            print("Do you need a help? use this command '!help'")
            Wait()

def Cart():
    flag = True
    while flag:
        pass
###############################
## OnlineShop Program Starts HERE! ##
###############################
MainMenu()