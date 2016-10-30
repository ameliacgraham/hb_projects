
shopping_list = []

def main():
    print "Type exit to exit \nType remove to remove an item"
    while(True):
        menu_choice = menu()
        if menu_choice == "0":
            menu()
        elif menu_choice == "1":
            sorted_list(shopping_list)
        elif menu_choice == "2":
            add_item()
        elif menu_choice == "3":
            break
        else:
            print "Please choose one of the options"
            menu()

def add_item():
    while(True):
        list_item = raw_input("Item to add: ").lower()
        if list_item == "exit":
            sorted_list(shopping_list)
            break
        elif list_item in shopping_list:
            print "Item is already on the list, enter a different item"
        elif list_item == 'remove':
            remove_item()
        else:
            shopping_list.append(list_item)

def sorted_list(s_list):
    shopping_list.sort()
    print shopping_list


def remove_item():
    item_removed = raw_input("Item to remove: ").lower()
    if item_removed in shopping_list:
        shopping_list.remove(item_removed)
    else:
        print "Item not in shopping list"
        remove_item()

def menu():
    selection = raw_input("0- Main Menu \n1- Show Current List \n2- Add an item to your shopping list \n3- Quit \n")
    return selection

if __name__ == "__main__":
    main()

