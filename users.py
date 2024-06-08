from main import OnlineShop
from tools import *
import getpass
from datetime import datetime

class Users:
    users_list = []

    def __init__(self, id, username, password, fname, lname, phone, isPhoneVerifyed, nationalId, dateOfBirth, role, lastLoginDate, address, cart):
        self.id = id
        self.username = username
        self.password = password
        self.fname = fname
        self.lname = lname
        self.phone = phone
        self.isPhoneVerifyed = isPhoneVerifyed
        self.nationalId = nationalId
        self.dateOfBirth = dateOfBirth
        self.role = role
        self.lastLoginDate = lastLoginDate
        self.address = address
        self.cart = cart

    def SearchUser(username, password, id): 
        for user in Users.users_list:
            if (user[1] == username and user[2] == password) or user[0] == id:
                selectedUser = Users(user[0], user[1], user[2], user[3], user[4], user[5],user[6],user[7],user[8],user[9],user[10],user[11],user[12])
                # Write in theLatestLoginUserId the Latest user logged in
                with open("DB\\user_db\\theLatestLoginUserId.txt","w") as file:
                    file.write(user['id'])
                    file.close()

                return selectedUser



    def UsersUpdate():
        Users.users_list = []
        with open('DB\\user_db\\users.txt','r') as file:
            for line in file.readlines():
                Users.users_list.append(eval(line))

    def LastUserID():
        Users.UsersUpdate()
        if Users.users_list == []:
            return 1
        lastUserId = int(Users.users_list[-1]['id'])
        return lastUserId + 1


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