from tools import *
from item import Item
from user import Users
from category import Category

class OnlineShop:
    items_list = []
    users_list = []
    selectedUser = ""
    logged_in = False
    isAdmin = False

    @classmethod
    def ShowMainMenu(cls):
        with open("DB\\user_db\\the_latest_login_id.txt","r") as file:
            lastLoginId = file.read()
            if lastLoginId != "":
                cls.selectedUser = Users.SearchUser(id = int(lastLoginId))
                #Users.write_the_latest_user_id(cls.selectedUser.user_id)
                if cls.selectedUser.role == 1:
                    cls.isAdmin = True
                cls.logged_in = True

        if cls.logged_in == False:
            print(ColoredNotification("You are not logged in!", "red"))
            print(ColoredNotification("Sign In | Sign UP", "green"))
        else:
            # When Admins Enter
            if cls.selectedUser.role == 1:
                print(ColoredNotification(cls.selectedUser.fname + " " + cls.selectedUser.lname,"cyan"))
                print(ColoredNotification("Admin Panel: Item | Category | User | Log Order","red"))
                print(ColoredNotification("Cart(0) | Sign Out | Categories | Search", "green"))

            # When Normal Users Enter
            else:
                print(ColoredNotification(cls.selectedUser.fname + " " + cls.selectedUser.lname,"cyan"))
                print(ColoredNotification("Cart(0) | Sign Out | Categories | Search", "green"))

    @classmethod
    def MainMenu(cls):
        mainMenuFlag = True
        while mainMenuFlag:
            ClearTerminal()
            cls.ShowMainMenu()
            answer = input(ColoredNotification("> ", "cyan")).lower()
            if cls.logged_in: # Logged-in
                
                if answer == "cart":
                    pass
                
                elif answer == "sign out":
                    if cls.logged_in == False:
                        print(ColoredNotification("You are not signed in!!!","red"))
                        Wait()
                    else:
                        Users.write_the_latest_user_id("")
                        cls.logged_in = False
                        cls.selectedUser = ""
                        print(ColoredNotification("You are signed out Successfully!!!", "green"))
                        Wait()

                elif cls.isAdmin: # Admin Enters
                    if answer == "item":
                        Item.ItemMenu()
                    elif answer == "category":
                        Category.category_menu()
                    elif answer == "user":
                        Users.user_managment_menu()
                    elif answer == "!help":
                        pass
                    else:
                        print("Do you need a help? use this command '!help'")
                        Wait()
                    

            else: # Not Logged-in
                if answer == "sign up":
                    Users.SignUpMenu()
                elif answer == "sign in":
                    if Users.SignInMenu() == True:
                        cls.logged_in = True

                


        
##########################
## Program Starts HERE! ##
##########################
if __name__ == "__main__":
    OnlineShop.MainMenu()