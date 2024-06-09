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
    def SearchUser(cls, show_results: bool = None, username: str = None, password: str = None, id: int = None):
        """
        Parameters:
        show_results (bool): True - Show Result
        """
        users_list = Users.get_users_list()
        if username and password:  # Search by username and password
            for user in users_list:
                if user['username'] == username and user['password'] == password:
                    if show_results: #TODO: Develope this part
                        pass
                    
                    selectedUser = cls(user['user_id'],
                                       user['username'],
                                       user['password'],
                                       user['fname'],
                                       user['lname'],
                                       user['phone'],
                                       user['role'],
                                       user['balance'],
                                       user['cart_id'])
                    return selectedUser
                
            if show_results: 
                print(ColoredNotification("User Not Found","red"))
                Wait()

            return None
        
        elif id:  # Search by user_id
            for user in users_list:
                if user['user_id'] == id:
                    if show_results: #TODO: Develope this part
                        pass
                    
                    selectedUser = cls(user['user_id'],
                                       user['username'],
                                       user['password'],
                                       user['fname'],
                                       user['lname'],
                                       user['phone'],
                                       user['role'],
                                       user['balance'],
                                       user['cart_id'])
                    return selectedUser
                
            if show_results: 
                print(ColoredNotification("User Not Found","red"))
                Wait()

            return None


    def get_users_list():
        users_list = []
        with open('DB\\user_db\\users.txt','r') as file:
            for line in file.readlines():
                users_list.append(eval(line))
            return users_list

    def LastUserID():
        users_list = Users.get_users_list()
        if users_list == []:
            return 1
        lastUserId = int(users_list[-1]['user_id'])
        return lastUserId + 1
    
    def write_the_latest_user_id(the_latest_id):
        # Write in theLatestLoginUserId the Latest user logged in
        with open("DB\\user_db\\the_latest_login_id.txt","w") as file:
            file.write(str(the_latest_id))

    @classmethod
    def SignUpMenu(cls):    
        ClearTerminal()
        print(ColoredNotification("Sign Up","green"))
        userId = Users.LastUserID()
        username = input("Username: ")
        password = input("Password: ")
        fname = input("First Name: ")
        lname = input("Last Name: ")
        phone = input("Phone Number: ")
        role = 0
        balance = 0
        cart_id = 0 #TODO: Get Cart ID for user
        
        # TODO: IF username exists
        selectedUser = cls(userId, username, password, fname, lname, phone,role,balance,cart_id)
        with open("DB\\user_db\\users.txt","a") as file:
            file.write(f"{selectedUser.__dict__}\n")
        
        with open("DB\\user_db\\the_last_id_created.txt","w") as file:
            file.write(str(userId))

        cls.write_the_latest_user_id(userId)

    def SignInMenu():
        ClearTerminal()
        print(ColoredNotification("Sign In", "green"))
        username = input("Username: ")
        password = getpass.getpass("Password: ")
        selectedUser = Users.SearchUser(show_results=True,username=username,password=password)
        if selectedUser != None:
            Users.write_the_latest_user_id(selectedUser.user_id)
            return True