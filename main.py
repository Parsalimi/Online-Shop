from tools import *
from item import Item
from user import Users
from category import Category
from cart import Cart
from order import Order

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
            print(ColoredNotification("Online Shop Program", "cyan"))
            print(ColoredNotification("You are not logged in!", "red"))
            print(ColoredNotification("Sign In | Sign UP", "green"))
        else:
            # When Admins Enter
            if cls.selectedUser.role == 1:
                print(ColoredNotification(cls.selectedUser.fname + " " + cls.selectedUser.lname,"cyan"))
                print(ColoredNotification("Admin Panel: Item | Category | User | UserOrder","red"))
                print(ColoredNotification(f"Cart({Cart.count_items_in_cart(cls.selectedUser.cart_id)}) | Shop | Order | Sign Out", "green"))

            # When Normal Users Enter
            else:
                print(ColoredNotification(cls.selectedUser.fname + " " + cls.selectedUser.lname,"cyan"))
                print(ColoredNotification(f"Cart({Cart.count_items_in_cart(cls.selectedUser.cart_id)}) | Shop | Order | Sign Out", "green"))

    @classmethod
    def MainMenu(cls):
        mainMenuFlag = True
        while mainMenuFlag:
            ClearTerminal()
            cls.ShowMainMenu()
            answer = input(ColoredNotification("> ", "cyan")).lower()
            if cls.logged_in: # Logged-in
                if answer == "shop":
                    cls.user_shopping_menu()
                
                elif answer == "cart":
                    cls.cart_menu()

                elif answer == 'order':
                    Order.show_user_orders(cls.selectedUser.order_ids)
                    Wait()

                elif answer == "sign out":
                        Users.write_the_latest_user_id("")
                        cls.logged_in = False
                        cls.selectedUser = ""
                        print(ColoredNotification("You are signed out Successfully!!!", "green"))
                        Wait()

                elif cls.isAdmin == False:
                    print(ColoredNotification("HELP:\n'cart' to manage Cart\n'shop' to buy items\n'order' to see list of your orders\n'sign out' to SIGN OUT", "red"))
                    Wait()

                elif cls.isAdmin: # Admin Enters
                    if answer == "item":
                        Item.ItemMenu()
                    elif answer == "category":
                        Category.category_menu()
                    elif answer == "user":
                        Users.user_managment_menu()
                    elif answer == 'userorder':
                        ClearTerminal()
                        Users.show_users()
                        
                        notcheck = True
                        while notcheck:
                            tagged = False
                            user_id = get_input(1, "Please enter the User ID to view their orders: ")
                            
                            if user_id not in Users.available_users_id():
                                print(ColoredNotification("That user does not exist!!!", "red"))
                                Wait()
                                tagged = True
                            
                            if tagged == False:
                                notcheck = False
                                
                        user_orders = Users.find_user_orders(user_id)
                        Order.show_user_orders(user_orders)
                        Wait()
                    else:
                        print(ColoredNotification("HELP:\n'item' to Manage Items\n'category' to Manage Categories\n'user' to manage Users\n'userorder' to see Orders of users\n'cart' to manage Cart\n'shop' to buy items\n'order' to see list of your orders\n'sign out' to SIGN OUT", "red"))
                        Wait()
                

            else: # Not Logged-in
                if answer == "sign up":
                    Users.SignUpMenu()
                elif answer == "sign in":
                    if Users.SignInMenu() == True:
                        cls.logged_in = True
                else:
                    print(ColoredNotification("Enter 'sign up' to SIGN UP & 'sign in' to SIGN IN", "red"))
                    Wait()
        
    @classmethod
    def user_shopping_menu(cls):
        while True:
            ClearTerminal()
            choice = (input(ColoredNotification("Shopping\nFilter | Exit\nFeel free to type anything to search\n> ","cyan"))).lower()
            if choice == 'exit':
                break
            elif choice == 'filter':
                possible_id_to_select = Item.user_search_item_menu(cls.selectedUser.age)
                if len(possible_id_to_select) > 0:
                    item_id = get_input(1,"(0 to exit)\nEnter Item ID that you want to buy: ",return_none_on='0',valid_options=possible_id_to_select)
                    if item_id:
                        if Cart.check_is_item_id_exists_in_cart(cls.selectedUser.cart_id, Item.convert_item_id_to_name(item_id)) == False:
                            buy_count = get_input(1,"How many Item do you want to buy: ")
                            Item.item_id_to_buy_it(item_id, cls.selectedUser.age, buy_count, cls.selectedUser.cart_id)
                        else:
                            ClearTerminal()
                            print(ColoredNotification(f"You have already select {Item.convert_item_id_to_name(item_id)}\nYou can edit it in your Cart.","red"))
                            Wait()
                else:
                    ClearTerminal()
                    print(ColoredNotification("No Result!!!", "red"))
                    Wait()
            else:
                possible_id_to_select = Item.user_free_search(choice, cls.selectedUser.age)
                if len(possible_id_to_select) > 0:
                    item_id = get_input(1,"(0 to exit)\nEnter Item ID that you want to buy: ",return_none_on='0',valid_options=possible_id_to_select)
                    if item_id:
                        if Cart.check_is_item_id_exists_in_cart(cls.selectedUser.cart_id, Item.convert_item_id_to_name(item_id)) == False:
                            buy_count = get_input(1,"How many Item do you want to buy: ")
                            Item.item_id_to_buy_it(item_id, cls.selectedUser.age, buy_count, cls.selectedUser.cart_id)
                        else:
                            ClearTerminal()
                            print(ColoredNotification(f"You have already select {Item.convert_item_id_to_name(item_id)}\nYou can edit it in your Cart.","red"))
                            Wait()
                else:
                    print(ColoredNotification("No Result!!!", "red"))
                    Wait()

    @classmethod
    def cart_menu(cls,):
        flag = True
        while flag:
            ClearTerminal()
            print(ColoredNotification("Cart Menu:", "cyan"))
            choice = (input(ColoredNotification("Show | Edit | Remove | checkout | Exit\n> ", "green"))).lower()
            if choice == 'exit':
                flag = False
                break
            elif choice == 'show':
                Cart.show_cart(1,cls.selectedUser.cart_id)
            elif choice == "remove":
                Cart.remove_product_from_cart(cls.selectedUser.cart_id)
            elif choice == "edit":
                Cart.edit_product_of_cart(cls.selectedUser.cart_id)
            elif choice == 'checkout':
                cart_list_name_count = Cart.cart_item_name_and_count_list(cls.selectedUser.cart_id)
                if cart_list_name_count:
                    if Item.remove_cart_items(cart_list_name_count) == False:
                        continue
                    else:
                        Cart.cart_checkout(cls.selectedUser.cart_id)

            
##########################
## Program Starts HERE! ##
##########################
if __name__ == "__main__":
    OnlineShop.MainMenu()