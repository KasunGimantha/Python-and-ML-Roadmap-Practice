contacts = {}
def add_contact(contacts, name, phone):

    return contacts

def view_contacts(contacts):
    return contacts


def delete_contact(contacts, name):
   return contacts


def search_contact(contacts, name):
   return contacts


def main_menu():
    global input_msg
    
    print("\n1. Add Contact\n")
    print("2. View Contacts\n")
    print("3. Search Contact\n")
    print("4. Delete Contact\n")
    print("5. Exit\n")
    input_msg = input("Enter Command: ")
    
    return input_msg
while True:   
    main_menu()
    
    while True:
        if input_msg == "1":
            
            for _ in range(3):
                
                name = input("Enter name: ")
                phone = input("Input phone numbner: ")
                
                contacts[name] = phone
               
                
            add_contact(contacts,name,phone) 
                   
        elif input_msg == "2":
            
            print(view_contacts(contacts))
            
        elif input_msg == "3":
            pass
        elif input_msg == "4":
            pass
        elif input_msg == "5":
            exit()
        else:
            print("\ninvalid command!!! ")
            main_menu()
        

