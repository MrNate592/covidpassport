import random
import pyfiglet                                                                    #importing all the modules
import csv
import time

profile_file_username = 'username.txt'                                            
profile_file_password = 'password.txt'


def register():
    global profile_file_username
    global profile_file_password

    with open(profile_file_username, 'w') as f:
        username = input("Enter new username: ")                                #prompts user to register by entering a password and username.                    
        f.write(username)
    with open(profile_file_password, 'w') as r:
        password = input("Enter new password: ")
        r.write(password)


def enter_profile_info():
    global profile_file_username
    global profile_file_password
    count = 0

    while True:
        count += 1
        if count > 3:                                                       # Retries three times if password and username are wrong.           
            quit()
        else:
            username = input("Enter username: ")
            password = input("Enter password: ")
            with open(profile_file_username, 'r') as f:
                for row in f:
                    r = row
            with open(profile_file_password, 'r') as q:
                for row1 in q:
                    r1 = row1
            if username == r and password == r1:                          #if password and username are correct it prints Welcome with the username.If not it prints retry username or password is incorrect!
                print("\n")
                print("Welcome Back " + username)
                print("\n")
                print(text)
                break
            else:
                print("Retry , username or password is incorrect!")


#Define variables
person_fields = ['ID', 'name', 'dob Month/Day/Year', 'vaccine', 'gender M/F', 'address', 'batch_no.', 'phone', 'blood_type', 'country']
person_database = 'person.csv'


#Prints 'ID CARD PYTHON' using the pyfiglet module
text = "Vaccine Database"
text2 = "Thank you for using our python project"
text = pyfiglet.figlet_format(text)



#Use of functions. Here this function shows the main menu.

def display_menu():
    print("1. Add New Person")
    print("2. View Persons")
    print("3. Search Person")
    print("4. Update Person")
    print("5. Delete Person")
    print("6. Create Vaccine Passport")
    print("7. Quit")

#Here this function adds a person to the database.

def add_person():
    print("-------------------------")
    print("Add Person's Information")
    print("-------------------------")
    global person_fields
    global person_database

    iden = random.randint(10000, 90000)                                     #A random 5 digit number is generated and appended to a list and the user must use this when adding a person.
    idlist = [iden]

    person_data = []

    print("Use this ID", iden)


    for field in person_fields:
        value = input("Enter " + field + ": ")                              #for every field specified in person_fields the program prompts the user to input a value and they are appended.
        person_data.append(value)
    with open(person_database, "a", encoding="utf-8") as f:                 #The database opened and the data is written into it and stored.
        writer = csv.writer(f)
        writer.writerows([person_data])

    print("Information saved successfully")
    input("Press any key to continue")
    return


#Here this function adds a person to the database.

def view_persons():
    global person_fields
    global person_database

    print("--- Database Records ---")
    with open(person_database, "r", encoding="utf-8") as f:          #This opens the database and prints every single row and column with their respective headings.
        reader = csv.reader(f)
        for x in person_fields:
            print(x, end='\t |')
        print("\n--------------------------------------------------------------------------------------------------------------------------------------------------")

        for row in reader:
            for item in row:
                print(item, end="\t |")
            print("\n")

    input("Press any key to continue")

#Here this function searches for a person.
def search_person():
    global person_fields
    global person_database

    print("1. Search Person's info by ID")                        #The user has two choices, either to search by ID number or by qr code.
    print("2. Search Person's info by qrcode")

    srchoice = input("Enter the number of your choice: ")
    if srchoice == '1':
        search_person_info_name()
    if srchoice == '2':
        import scanqr as qrcode


def search_person_info_name():
    global person_database

    print("--- Search Patient's Info via ID ---")
    ID = input("Enter ID of Person to search: ")
    with open(person_database, "r", encoding="utf-8") as f:                          #The user is asked to enter the ID. The database is opened and it searches for it. When the ID is found all the respective data for that person is printed.
        reader = csv.reader(f)
        for row in reader:
            if len(row) > 0:
                if ID == row[0]:
                    print("----- Person Found -----")
                    print("ID: ", row[0])
                    print("Name: ", row[1])
                    print("Dob: ", row[2])
                    print("Vaccine: ", row[3])
                    print("Gender: ", row[4])
                    print("Address: ", row[5])
                    print("Batch Number: ", row[6])
                    print("Phone: ", row[7])
                    print("Blood Type: ", row[8])
                    print("Country: ", row[9])
                    break
        else:
            print("ID not found in our database")           #If the ID entered does not match with any person in the database it prints Patient of such name not found in our database.
            input("Press any key to continue")


#Here this function updates a person's information.
def update_person():
    global person_fields
    global person_database

    print("--- Update person ---")
    ID = input("Enter ID to update: ")
    index_person = None
    updated_data = []
    with open(person_database, "r", encoding="utf-8") as f:                #The user is asked to enter the ID. The database is opened and it searches for it. When the ID is found the user is asked to change the data.The new data is appended to the database.
        reader = csv.reader(f)
        counter = 0
        for row in reader:
            if len(row) > 0:
                if ID == row[0]:
                    index_person = counter
                    print("person Found: at index ",index_person)
                    person_data = []
                    for field in person_fields:
                        value = input("Enter " + field + ": ")
                        person_data.append(value)
                    updated_data.append(person_data)
                else:
                    updated_data.append(row)
                counter += 1


    # Check if the record is found or not
    if index_person is not None:
        with open(person_database, "w", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(updated_data)
    else:
        print("ID not found in our database")
        input("Press any key to continue")



#Here this function deletes a person's information.
def delete_person():
    global person_fields
    global person_database

    print("--- Delete person ---")
    ID = input("Enter ID to delete: ")
    person_found = False
    updated_data = []
    with open(person_database, "r", encoding="utf-8") as f:          #The user is asked to enter the ID. The database is opened and it searches for it. When the ID is found the person is deleted.
        reader = csv.reader(f)
        counter = 0
        for row in reader:
            if len(row) > 0:
                if ID != row[0]:
                    updated_data.append(row)
                    counter += 1
                else:
                    person_found = True

    if person_found is True:
        with open(person_database, "w", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(updated_data)
        print("ID no. ", ID , "deleted successfully")
    else:
        print("ID not found in our database")
        input("Press any key to continue")
        

print("1. Sign in")                                                     #This is part of the password system which prompts the user to either register or sign in.
print("2. Register")
 
pchoice = input("Please enter number of your choice: ")

if pchoice == '1':
    enter_profile_info()
if pchoice == '2':
    register()
    enter_profile_info()



while True:
    display_menu()

    choice = input("Enter your choice: ")
    if choice == '1':
        add_person()
    elif choice == '2':
        view_persons()                                    #Based on user inputs the program will execute the respective functions.
    elif choice == '3':
        search_person()
    elif choice == '4':
        update_person()
    elif choice == '5':
        delete_person()
    elif choice == '7':
        text2 = pyfiglet.figlet_format(text2)
        print(text2)
        time.sleep(4)
        quit()
    elif choice == '6':
        import passport







































