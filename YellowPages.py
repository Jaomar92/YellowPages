#Student: Jeffey Aroun bin Omar

#Initialization of DataBase
yellow_pages = { 
    "C":[{"nama":"Chandra", "hp":"6282127289952", "kota":'jakarta Barat', "zip":'132190'}],
    "D":[{"nama":"Dita Claudia", "hp":"628111366828", "kota":'jakarta Selatan', "zip":'12190'}],
    "F":[
    {"nama":"Fuad", "hp":"6281482228265", "kota":'jakarta Selatan', "zip":'668258'},
    {"nama":"Fatima", "hp":"6282242807286", "kota":'jakarta timur', "zip":'599872'},
    ],
    "J":[{"nama":"Jeffrey Omar", "hp":"085219787939", "kota":'jakarta Selatan', "zip":'12190'}], 
    "K":[{"nama":"Karina Farida", "hp":"6281515745925", "kota":'Depok', "zip":'294522'}],
   
    
}



def Greeting():
    print("Halo Selamat Datang ke Jeffrey punya Python Yello Pages Program! ")
    print("Bagai Mana saya bisa Bantu anda? ")

# Funtion to print Menu Options
def Menu():
    print('''
    MENU:-
    Sila pulih opsi

    1. add Contact.
    2. Update Contact.
    3. Delete Contact.
    4. Search Contact.
    5. Keluar.
    ''')
def organize_options():
    
    state = True
    while state:
        print('''
    How would you prefer retrieve your desired contact.
    1. All contacts listed.
    2. By Alphabet
    3. By Person.
    4. Exit.
    ''') 
        userOption = input("Input from 1 - 4: ")
        if userOption == "1":
            print(' ')
            print("Contact List:- ")
            # organize the alphabets
            organized = dict(sorted(yellow_pages.items()))
            #Organize the dictionary of the alphabets
            for i in organized:
            #use sorted based on keys
                organized[i]= sorted(yellow_pages[i], key=lambda d: d['nama'])
                if len(organized[i]) > 0:
                    print(i)
                else:
                    continue
                for j in organized[i]:
                    print('  ', j['nama'],'\n','|',"contact: ", j['hp']," "*(15 -len(j['hp'])), "|", "kota: ", j['kota']," "*(15 -len(j['kota'])), "|" ,"zip: ", j['zip']," "*(7 -len(j['zip'])), "|")
                    print('--------------------------------------------------------------------------')
                print()
            print('^^^ Scroll up ^^^')
            
        elif userOption == "2":
            contactAlph = input('What alphabet tab would you like to check? ').title()
            N = contactAlph[0] if contactAlph[0].isalpha() else '#'
            count = 0 
            print('\n ')
            print(f"Contact List of {N}:- ")
            if yellow_pages.get(N) is not None:
                print(N)
                for i in yellow_pages[N]:
                    print('  ', i['nama'],'\n','|',"contact: ", i['hp']," "*(15 -len(i['hp'])), "|", "kota: ", i['kota']," "*(15 -len(i['kota'])), "|" ,"zip: ", i['zip']," "*(7 -len(i['zip'])), "|")
                    print('--------------------------------------------------------------------------')
                    count += 1
                print('\n')
                print(f"Number of contact list in alpha tab {N} is {count} people.")
            else:
                print('\n')
                print(f"No one exist in the alphabet tab of {N}")
                print('\n')
                print('Please return to search contact Menu.')
                print('\n')

        elif userOption == '3':
            contactName = input('Who would you like to check? ').title()
            N = contactName[0] if contactName[0].isalpha() else '#'
            for i in yellow_pages[N]:
                if (contactName == i['nama']):
                    print('  ', i['nama'],'\n','|',"contact: ", i['hp']," "*(15 -len(i['hp'])), "|", "kota: ", i['kota']," "*(15 -len(i['kota'])), "|" ,"zip: ", i['zip']," "*(7 -len(i['zip'])), "|")
                    print('--------------------------------------------------------------------------')
                    
            print('\n')
            print("!!!<-----Contact not found----->!!!")
            if yellow_pages[N]:
                print('You could try search for these names instead: - ')
                print('\n')           
                for i in yellow_pages[N]:
                    print(i["nama"])
            print('\n')           
            
        elif userOption == "4":
            print('Returning to main programing')
            state = False

        else:
            print('\n')
            print("Input not valid.")
            print('\n')
            print('!!! ERROR !!!')
            print("Please Input a valid input of 1 - 4")

# Function to organize the dictionary. 
def organize_contact():
    print(' ')
    print("Contact List:- ")
    # organize the alphabets
    organized = dict(sorted(yellow_pages.items()))
    #Organize the dictionary of the alphabets
    for i in organized:
    #use sorted based on keys
        organized[i]= sorted(yellow_pages[i], key=lambda d: d['nama'])
        if len(organized[i]) > 0:
            print(i)
        else:
            continue
        for j in organized[i]:
            print('  ', j['nama'],'\n','|',"contact: ", j['hp']," "*(15 -len(j['hp'])), "|", "kota: ", j['kota']," "*(15 -len(j['kota'])), "|" ,"zip: ", j['zip']," "*(7 -len(j['zip'])), "|")
            print('--------------------------------------------------------------------------')
        print()


# Function to Add Contact
def Add_contact():
    state =True
    while state:
        # Take contact Details
        # first error check is name
        contactName = input("Name of the person you would like to add: ").title()
        # Get the first character of the name
        # checks if N is an alphabet or something else.
        N = contactName[0] if contactName[0].isalpha() else '#'
        # checks if N is in the yellow_pages dict.
        # if it is not it will create a new dict key.
        if N not in yellow_pages:
            yellow_pages[N] = []
        # Checks if user already exist

        for i in yellow_pages[N]:
            if (contactName == i['nama']):
                print('\n')
                print("!!!<---- User already exists ---->!!!!")
                print('\n')
                state = False
                return state
        # continues if all is in order. 
        contactNum = input("what is the contact number: ")
        contactKota = input("contact Kota: ")
        contactZip = input("Contact zip: ")
        yellow_pages[N].append({'nama':contactName, 'hp':contactNum, 'kota':contactKota, 'zip':contactZip})
        state = False
# Update Contact


def Update_contact():
    organize_contact()
    #Get user contact they wish to update.
    contactName = input("Enter the name of the contact you would like to delete: ").title()
    # Checks if its a alphabet or char.
    N = contactName[0] if contactName[0].isalpha() else '#'
    for i in yellow_pages[N]:
        if (contactName == i['nama']):
            i['hp'] = input("Enter the updated contact number: ")
            i['kota'] = input("Enter the updated city: ")
            i['zip'] = input("Enter the updated zip: ")
            print("Contact has been updated successfully")
            return
    print('\n')
    print("!!!<-----Contact not found----->!!!")
    print('\n')

# Delete contact
def Delete_contact():
    #prints current contact list for better reference
    organize_contact()
    # Ask user which contact they want to delete.
    contactName = input("Enter the name of the contact you would like to delete: ").title()
    # checks if the contact exsist.
    N = contactName[0] if contactName[0].isalpha() else '#'
    # iterates contact list to find a match
    for i in yellow_pages[N]:
        if (contactName == i['nama']):
            yellow_pages[N].remove(i)
            print("Contact has been deleted successfully")
            return
    print('\n')
    print("!!!<-----Contact not found----->!!!")
    print('\n')


# organize_contact()
Greeting()
while True:
    Menu()
    userOption = input(" Sila pilih nomur: ")
    userInput = int(userOption if userOption.isdigit() else 6)
    if (userInput == 1):
        print("Anda pilih: " + str(userOption))
        Add_contact()
    elif (userInput == 2):
        print("Anda pilih: " + str(userOption))
        Update_contact()
    elif (userInput == 3):
        print("Anda pilih: " + str(userOption))
        Delete_contact()
    elif (userInput == 4):
        print("Anda pilih: " + str(userOption))
        organize_options()
    elif (userInput == 5):
        print("Anda pilih: " + str(userOption))
        break
    else:
        print('\n')        
        print("!!!<---Pilihan yang anda masukkan salah. Silakan coba lagi.--->!!! ")
        print('\n')        
