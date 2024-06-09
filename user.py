# user_id | username | password | fname | lname | phone | role | balance | cart_id #9
from tools import *
import getpass
from datetime import datetime

class Users:
    def __init__(self, user_id, username, password, fname, lname, phone, role, balance, cart_id):
        self.user_id = user_id
        self.username = username
        self.password = password
        self.fname = fname
        self.lname = lname
        self.phone = phone
        self.role = role
        self.balance = balance
        self.cart_id = cart_id

    @classmethod
    def SearchUser(cls, users_list, show_results: bool = None, username: str = None, password: str = None, id: int = None):
        """
        Parameters:
        show_results (bool): True - Show Result
        """
        if username and password:  # Search by username and password
            for user in users_list:
                if user['username'] == username and user['password'] == password:
                    if show_results: #TODO: Develope this part
                        pass
                    selectedUser = cls(eval(user.strip()))
                    return selectedUser
                
            if show_results: 
                print("User Not Found")

            return None
        
        elif id:  # Search by user_id
            for user in users_list:
                if user['user_id'] == id:
                    if show_results: #TODO: Develope this part
                        pass
                    
                    selectedUser = cls(eval(user.strip()))
                    return selectedUser
                
            if show_results: 
                print("User Not Found")

            return None


    def UsersUpdate():
        users_list = []
        with open('DB\\user_db\\users.txt','r') as file:
            for line in file.readlines():
                users_list.append(eval(line))
            return users_list

    def LastUserID():
        Users.UsersUpdate()
        if Users.users_list == []:
            return 1
        lastUserId = int(Users.users_list[-1]['id'])
        return lastUserId + 1
    
    def write_the_latest_user_id(the_latest_id):
        # Write in theLatestLoginUserId the Latest user logged in
        with open("DB\\user_db\\the_latest_login_id.txt","w") as file:
            file.write(the_latest_id)


    #############################################################################################################
    ################################################## USERS ####################################################
    ## id, username, password, fname, lname, phone, isPhoneVerifyed, nationalId, dateOfBirth, role, last login, address, cart ##
    #############################################################################################################
    #############################################################################################################

    def SignUpMenu():    
        ClearTerminal()
        print(Fore.GREEN + "Sign Up")
        userId = Users.LastUserID()
        username = input("Username: ")
        password = input("Password: ")
        fname = input("First Name: ")
        lname = input("Last Name: ")
        phone = input("Phone Number: ")
        address = input("Address: ")
        # TODO: IF username exists
        OnlineShop.selectedUser = Users(userId, username, password, fname, lname, phone,"","","","0",datetime.now(),address,"")
        with open("DB\\users.txt","a") as file:
            file.write(f"{OnlineShop.selectedUser.__dict__}\n")
        
        with open("DB\\theLatestLoginUserId.txt","w") as file:
            file.write(str(userId))
            file.close()

    def SignInMenu():
        ClearTerminal()
        Users.UsersUpdate()
        print(Fore.GREEN + "Sign In" + Fore.WHITE )
        username = input("Username: ")
        password = getpass.getpass("Password: ")
        Users.SearchUser(username,password,"")