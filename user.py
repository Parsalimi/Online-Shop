# user_id | username | password | fname | lname | age | phone | role | order_ids | cart_id #10
from tools import *
import getpass
from prettytable import PrettyTable
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
            username = get_input(3, "Username: ")
            if ' ' not in list(username) and "\\" not in list(username):
                if username:
                    # Check if that username exists
                    for user in users_list:
                        if user['username'].lower() == username:
                            print(ColoredNotification("That username is already EXISTS!!!", "red"))
                            Wait()  
                            ClearTerminal()
                            tagged = True
                else:
                    print(ColoredNotification("Enter something!!!", "red"))
                    Wait()
                    ClearTerminal()
                    tagged = True
                
                if tagged == False:
                    notcheck = False
            else:
                    print(ColoredNotification("You cant use space or '\\'!!!", "red"))
                    Wait()
                    ClearTerminal()
                    tagged = True
        
        # Password
        notcheck = True
        while notcheck:
            tagged = False
            password = input("Password: ")
            if ' ' not in list(password) and "\\" not in list(password):
                if password:
                    pass
                else:
                    print(ColoredNotification("Enter something!!!", "red"))
                    Wait()
                    ClearTerminal()
                    tagged = True
                
                if tagged == False:
                    notcheck = False
            else:
                    print(ColoredNotification("You cant use space or '\\'!!!", "red"))
                    Wait()
                    ClearTerminal()
                    tagged = True

        # First Name
        notcheck = True
        while notcheck:
            tagged = False
            fname = get_input(4, "First Name: ")
            if ' ' not in list(fname) and "\\" not in list(fname):
                if fname:
                    pass
                else:
                    print(ColoredNotification("Enter something!!!", "red"))
                    Wait()
                    ClearTerminal()
                    tagged = True
                
                if tagged == False:
                    notcheck = False
            else:
                    print(ColoredNotification("You cant use space or '\\'!!!", "red"))
                    Wait()
                    ClearTerminal()
                    tagged = True

        # Last Name
        notcheck = True
        while notcheck:
            tagged = False
            lname = get_input(4, "Last Name: ")
            if ' ' not in list(lname) and "\\" not in list(lname):
                if lname:
                    pass
                else:
                    print(ColoredNotification("Enter something!!!", "red"))
                    Wait()
                    ClearTerminal()
                    tagged = True
                
                if tagged == False:
                    notcheck = False
            else:
                    print(ColoredNotification("You cant use space or '\\'!!!", "red"))
                    Wait()
                    ClearTerminal()
                    tagged = True 

        # Age
        notcheck = True
        while notcheck:
            tagged = False
            age = get_input(1,"Age: ")
            if age:
                    if age < 0 or age > 120:
                        print(ColoredNotification("Invalid Age!!!", "red"))
                        Wait()
                        ClearTerminal()
                        tagged = True
                    else:
                        notcheck = False
            else:
                print(ColoredNotification("Enter something!!!", "red"))
                Wait()
                ClearTerminal()
                tagged = True
            
            if tagged == False:
                notcheck = False
                    

        # Phone Number
        notcheck = True
        while notcheck:
            tagged = False
            phone = get_input(5, "Phone Number: ")
            if ' ' not in list(phone) and "\\" not in list(phone):
                if phone:
                    if len(phone) != 11:
                        tagged = True
                        print(ColoredNotification("Phone must be 11", "red"))
                        Wait()     
                else:
                    print(ColoredNotification("Enter something!!!", "red"))
                    Wait()
                    ClearTerminal()
                    tagged = True
                
                if tagged == False:
                    notcheck = False
            else:
                    print(ColoredNotification("You cant use space or '\\'!!!", "red"))
                    Wait()
                    ClearTerminal()
                    tagged = True    

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
        username = input("(enter to quit)\nUsername: ")
        if username:
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
            print(ColoredNotification("Remove | Edit | Show | Search | Exit", "green"))
            answer = input(ColoredNotification("> ", "cyan")).lower()
            if answer == "remove":
                cls.remove_user()
            elif answer == "edit":
                cls.edit_user()
            elif answer == "show":
                cls.show_users()
            elif answer == "search":
                cls.search_user_menu()
            elif answer == "exit":
                user_menu_flag = False
                break
            else:
                print(ColoredNotification("Invalid Option", "red"))
                Wait()

    @classmethod
    def search_user(cls, users_list, search_by=None, search_value=None):
        table_row_list = []

        if search_by == 'id':
            for user in users_list:
                if user['user_id'] == search_value:
                    table_row_list.append([user['user_id'], user['username'], user['password'],user['fname'], user['lname'], user['age'], user['phone'], user['role'], user['order_ids'], user['cart_id']])
                    break
                
        elif search_by == 'username':
            for user in users_list:
                if user['username'].lower() == search_value:
                    table_row_list.append([user['user_id'], user['username'], user['password'],user['fname'], user['lname'], user['age'], user['phone'], user['role'], user['order_ids'], user['cart_id']])
                    break
                
        elif search_by == 'fname':
            for user in users_list:
                if user['fname'].lower() == search_value:
                    table_row_list.append([user['user_id'], user['username'], user['password'],user['fname'], user['lname'], user['age'], user['phone'], user['role'], user['order_ids'], user['cart_id']])

                
        elif search_by == 'lname':
            for user in users_list:
                if user['lname'].lower() == search_value:
                    table_row_list.append([user['user_id'], user['username'], user['password'],user['fname'], user['lname'], user['age'], user['phone'], user['role'], user['order_ids'], user['cart_id']])


        cls.create_table_user(table_row_list)

    def create_table_user(table_row_list: list):
        table = PrettyTable()
        table.field_names = ["ID", 'Username','Password','First Name','Last Name','Age','Phone','Role','Order_ids','Cart_id']
        for table_row in table_row_list:
            table.add_row([table_row[0], table_row[1], table_row[2], table_row[3], table_row[4], table_row[5], table_row[6], table_row[7], table_row[8], table_row[9]])
        print(table)
        Wait()

    @classmethod
    def search_user_menu(cls):
        ClearTerminal()
        users_list = cls.get_users_list()

        search_by = get_input(3, "(0 to exit)\nSearch By (id/username/fname/lname): ", ['id', 'username', 'fname', 'lname'], '0')
        search_value = None
        if search_by == "id":
            search_value = get_input(1,"user ID: ")
        elif search_by == 'username':
            search_value = get_input(3,"Username: ")
        elif search_by == 'fname':
            search_value = get_input(3,"First Name: ")
        elif search_by == 'lname':
            search_value = get_input(3,"Last Name: ")

        cls.search_user(users_list, search_by=search_by, search_value=search_value)
        
    @classmethod
    def remove_user(cls):
        users_list = cls.get_users_list()

        ClearTerminal()
        cls.show_users()
        user_id = get_input(1,"(0 to exit)\nEnter user ID to remove: ",return_none_on='0')
        if user_id:
            for index, user in enumerate(users_list):
                if user["user_id"] == int(user_id):
                    users_list.pop(index)

            cls.update_user_db(users_list)

    @classmethod
    def update_user_db(cls, users_list):
        with open('DB\\user_db\\users.txt', 'w') as file:
            for user in users_list:
                selectedUser = cls(user['user_id'], user['username'], user['password'],user['fname'], user['lname'], user['age'], user['phone'], user['role'], user['order_ids'], user['cart_id'])
                
                file.write(f'{selectedUser.__dict__}\n')

    @classmethod
    def show_users(cls):
        users_list = cls.get_users_list()
        ClearTerminal()
        print(ColoredNotification("Users Table", "green"))

        table = PrettyTable()
        table.field_names = ["ID", 'Username','Password','First Name','Last Name','Age','Phone','Role','Order_ids','Cart_id']
        for user in users_list:
                table.add_row([user['user_id'], 
                               user['username'], 
                               '****', 
                               user['fname'], 
                               user['lname'], 
                               user['age'], 
                               user['phone'], 
                               user['role'], 
                               user['order_ids'], 
                               user['cart_id']])
        print(table)
        Wait()

    @classmethod
    def edit_user(cls):
        users_list = cls.get_users_list()
        ClearTerminal()
        cls.show_users()
        user_id = get_input(1,"(0 to exit)\nEnter User ID to edit: ",valid_options=cls.available_users_id(),return_none_on='0')
        if user_id:
            for user in users_list:
                if user["user_id"] == int(user_id):
                    answer = get_input(3,"type these attributes to change them:\nusername | password | fname | lname | age | phone | role\n> ",valid_options=['username','password', 'fname', 'lname', 'age', 'phone','role'])
                    
                    if answer == "username":
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

                        user['username'] = username

                    elif answer == 'password':
                        user['password']

                    elif answer == 'fname':
                        notcheck = True
                        while notcheck:
                            fname = input("First Name: ")
                            if is_str_contains_int(fname):
                                print(ColoredNotification("Does your first name really have a number in it!?!", "red"))
                                Wait()
                                ClearTerminal()
                            else:
                                notcheck = False
                        user['fname'] = fname

                    elif answer == 'lname':
                        notcheck = True
                        while notcheck:
                            lname = input("Last Name: ")
                            if is_str_contains_int(lname):
                                print(ColoredNotification("Does your last name really have a number in it!?!", "red"))
                                Wait()
                                ClearTerminal()
                            else:
                                notcheck = False
                        user['lname'] = lname

                    elif answer == 'age':
                        notcheck = True
                        while notcheck:
                            age = get_input(1,"Age: ")
                            if age < 0 or age > 120:
                                print(ColoredNotification("Invalid Age!!!", "red"))
                                Wait()
                                ClearTerminal()
                            else:
                                notcheck = False
                        user['age'] = age

                    elif answer == 'phone':
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

                        user['phone'] = phone

                    elif answer == 'role':
                        user['role'] = get_input(1,"Role: ",valid_options=[0,1])
                    else:
                        print(ColoredNotification("Invalid", "red"))
                        Wait()

                    cls.update_user_db(users_list)
                    break
                
    @classmethod
    def available_users_id(cls):
        available_id_list = []
        users_list = cls.get_users_list()
        for user in users_list:
            available_id_list.append(int(user['user_id']))

        return available_id_list
    
    @classmethod
    def find_user_orders(cls, user_id):
        users_list = cls.get_users_list()
        for user in users_list:
            if user['user_id'] == user_id:
                return user['order_ids']

