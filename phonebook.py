import sys
def initial_phonebook():
    rows,cols=int(input("enter initial number of contacts : ")),5
    phonebook=[]
    print(phonebook)
    for i in range(rows):
        print("\nEnter contact %d detail in the following orders(ONLY):" %(i+1))
        print(" Note: * indicates mandatary fields")
        print("..........................................................")
        temp=[]
        for j in range(cols):
            if j ==0:
                temp.append(str(input("Enter name * = ")))
                if temp[j]=="" or temp[j]==" ":
                    sys.exit("Name is mandatory field. Exiting due to blank field...")
            if j == 1: 
                temp.append(int(input("Enter number * = "))) 
            if j == 2:
                temp.append(str(input("Enter e-mail address = "))) 
                if temp[j] == '' or temp[j] == ' ': 
                    temp[j] = None
            if j == 3: 
                temp.append(str(input("Enter date of birth (dd/mm/yyyy) = ")))
                if temp[j] == '' or temp[j] == ' ': 
                    temp[j] = None
            if j == 4: 
                temp.append (str(input("Enter category(Family/Friends/Work/Others): ")))
                if temp[j] == "" or temp[j] == ' ': 
                    temp[j] = None
        phonebook.append(temp)
    print(phonebook)
    return phonebook
def menu():
    print("*************************************************************")
    print("\t\t\t SMART PHONE DIRECTORY")
    print("*************************************************************")
    print("\tYou can now perform the following operations on this phonebook\n")
    print("1. Add a new contact")
    print("2. Remove an existing contact ")
    print("3. Delete all contacts")
    print("4. search for a contact")
    print("5. Display all contacts")
    print("6. Exit phonebook")
    choice = int(input(" Enter your choice : "))
    return choice
def Add_contact(pb):
    dip=[]
    for i in range (len(pb[0])):
        if i ==0:
            dip.append(str(input("Enter name * = ")))
        if i ==1:
            dip.append(int(input("Enter phone number * = ")))
        if i ==2:
            dip.append(str(input("Enter email = ")))
        if i ==3:
            dip.append(str(input("Enter date of birth (dd/mm/yyyy) = ")))
        if i ==4:
            dip.append(str(input("Enter category(family/friend/office/other) = ")))
    pb.append(dip)
    return pb