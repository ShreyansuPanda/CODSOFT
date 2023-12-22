contact={}

def display_contact():
    print("Name\t\tContact Number")
    for key in contact:
        print("{}\t\t{}".format(key,contact[key]))

while True:
    choice=int(input("1.Create a new \n 2. Search Contact \n 3.Display Contact \n 4.Edit Contact \n 5.Delete Contact \n 6.Exit \n Enter your choice: "))
    if choice==1:
        name=input("Enter the name: ")
        phone=input("Enter the mobile number: ")
        contact[name]=phone
    elif choice==2:
        search_name= input("Enter the contact name: ")
        if search_name in contact:
            print(search_name,"$ contact number is",contact[search_name])
        else:
            print("Name is not found in contact")
    elif choice==3:
        if not contact:
            print("Empty contact book")
        else:
            display_contact()
    elif choice==4:
        edit_contact=input("Enter the contact to be edited: ")
        if edit_contact in contact:
            phone=input("enter phone number:")
            contact[edit_contact]=phone
            print("Contact updated")
            display_contact()
        else:
            print("Name is not found in contact book ")
    elif choice ==5:
        del_contact= input("Enter the contact to be deleted")
        if del_contact in contact:
            confirm=input("Do you want to delete this contact y/n?")
            if confirm=='y' or confirm=='Y':
                contact.pop(del_contact)
            display_contact()
        else:
            print("Name is not found in contact book ")
    else:
        break



