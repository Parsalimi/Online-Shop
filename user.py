# user_id | username | password | fname | lname | age | phone | role | order_ids | cart_id #10
from tools import *
import getpass
from datetime import datetime
from cart import Cart

class Users:
    def __init__(self, user_id, username, password, fname, lname, age, phone, role, order_ids, cart_id):
        self.user_id = user_id
        self.username = username
        self.password = password
        self.fname = fname
        self.lname = lname
        self.age = age
        self.phone = phone
        self.role = role
        self.order_ids = order_ids
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
                                       user['age'],
                                       user['phone'],
                                       user['role'],
                                       user['order_ids'],
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
                                       user['age'],
                                       user['phone'],
                                       user['role'],
                                       user['order_ids'],
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
        users_list = Users.get_users_list()
        

        ClearTerminal()
        print(ColoredNotification("Sign Up","green"))
        userId = Users.LastUserID()

        notcheck = True
        while notcheck:
            tagged = False
            username = input("Username: ")
            # Check if that username exists
            for user in users_list:
                if user['username'] == username:
                    print(ColoredNotification("That username is already EXISTS!!!", "red"))
                    Wait()
                    ClearTerminal()
                    tagged = True
            
            if tagged == False:
                notcheck = False

        password = input("Password: ")
        notcheck = True
        while notcheck:
            fname = input("First Name: ")
            if is_str_contains_int(fname):
                print(ColoredNotification("Does your first name really have a number in it!?!", "red"))
                Wait()
                ClearTerminal()
            else:
                notcheck = False
            
        notcheck = True
        while notcheck:
            lname = input("Last Name: ")
            if is_str_contains_int(lname):
                print(ColoredNotification("Does your last name really have a number in it!?!", "red"))
                Wait()
                ClearTerminal()
            else:
                notcheck = False

        notcheck = True
        while notcheck:
            age = get_input(1,"Age: ")
            if age < 0 or age > 120:
                print(ColoredNotification("Invalid Age!!!", "red"))
                Wait()
                ClearTerminal()
            else:
                notcheck = False
        
        notcheck = True
        while notcheck:
            tagged = False
            phone = input("Phone Number: ")
            if len(phone) != 11:
                tagged = True

            for char in list(phone):
                if char.isdigit() == False:
                    tagged = True
                    break

            if tagged == False:
                notcheck = False
            else:
                print(ColoredNotification("Invalid Number!!!", "red"))
                Wait()
                ClearTerminal()

        role = 0
        order_ids = []
        cart_id = Cart.create_new_cart()
        
        
        selectedUser = cls(userId, username, password, fname, lname, age,phone,role,order_ids,cart_id)
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
        
    @classmethod
    def user_managment_menu(cls):
        ClearTerminal()
        user_menu_flag = True
        while user_menu_flag:
            ClearTerminal()
            print(ColoredNotification("User Management", "green"))
            print(ColoredNotification("Add | Remove | Edit | Show | Search | Exit", "green"))
            answer = input(ColoredNotification("> ", "cyan")).lower()
            if answer == "add":
                cls.add_user()
            elif answer == "remove":
                cls.remove_category()
            elif answer == "edit":
                cls.edit_category()
            elif answer == "show":
                cls.show_categories()
            elif answer == "search":
                cls.search_category_menu()
            elif answer == "exit":
                category_menu_flag = False
                break
            else:
                print(ColoredNotification("Invalid Option", "red"))
                Wait()

    def add_user():
        ClearTerminal()
        user_id = Users.LastUserID()

