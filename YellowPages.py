#Student: Jeffey Aroun bin Omar

#Initialization of DataBase
yellow_pages = { 
    "C":[{"nama":"Chandra", "hp":"6282127289952", "kota":'Jakarta Barat', "zip":'132190'}],
    "D":[{"nama":"Dita Claudia", "hp":"628111366828", "kota":'Jakarta Selatan', "zip":'12190'}],
    "F":[
    {"nama":"Fuad", "hp":"6281482228265", "kota":'Jakarta Selatan', "zip":'668258'},
    {"nama":"Fatima", "hp":"6282242807286", "kota":'Jakarta timur', "zip":'599872'},
    ],
    "J":[{"nama":"Jeffrey Omar", "hp":"085219787939", "kota":'Jakarta Selatan', "zip":'12190'}], 
    "K":[{"nama":"Karina Farida", "hp":"6281515745925", "kota":'Depok', "zip":'294522'}], 
}

# ==========================================================================================================================================================================================================
# Minor Functions START 
# ==========================================================================================================================================================================================================

def Greeting():
    print("Halo Selamat Datang di program Python Yellow Pages Jeffrey! ")
    print("Bisa saya bantu? ")

# Funtion to print Menu Options
def Menu():
    print('''
    MENU:-
    Silahkan pilih opsi

    1. Tambah Kontak.
    2. Perbaharui Kontak.
    3. Hapus Kontak.
    4. Cari Kontak.
    5. Keluar.
    ''')

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
# ==========================================================================================================================================================================================================
# Minor Functions END 
# ==========================================================================================================================================================================================================

# ==========================================================================================================================================================================================================
# Main Functions START 
# ==========================================================================================================================================================================================================

# ==========================================================================================================================================================================================================
# Add contact Start 
# ==========================================================================================================================================================================================================

# Function to Add Contact
def Add_contact():
    state =True
    while state:
        # Take contact Details
        # first error check is name
        contactName = input("Nama kontak yang anda ingin tambah: ").title()
        # Get the first character of the name
        # checks if N is an alphabet or something else.
        if len(contactName) == 0:
            print('Returning to Main Menu')
            state = False
            return state
        N = contactName[0] if contactName[0].isalpha() else '#'
        # checks if N is in the yellow_pages dict.
        # if it is not it will create a new dict key.
        if N not in yellow_pages:
            yellow_pages[N] = []
        # Checks if user already exist

        for i in yellow_pages[N]:
            if (contactName == i['nama']):
                print('\n')
                print("!!!<-- contact dengan nama yang di input sudah wujud. Anda di kembalikan ke menu utama. -->!!!!")
                print('\n')
                state = False
                return state
        # continues if all is in order. 
        contactNum = input("what is the contact number: ")
        if len(contactNum) == 0:
            print('Returning to Main Menu')
            state = False
            return state
        contactKota = input("contact Kota: ").title()
        if len(contactKota) == 0:
            print('Returning to Main Menu')
            state = False
            return state
        contactZip = input("Contact zip: ")
        if len(contactZip) == 0:
            print('Returning to Main Menu')
            state = False
            return state
        yellow_pages[N].append({'nama':contactName, 'hp':contactNum, 'kota':contactKota, 'zip':contactZip})
        state = False
# ==========================================================================================================================================================================================================
# Add Contact End 
# ==========================================================================================================================================================================================================

# ==========================================================================================================================================================================================================
# Update Contac Start 
# ==========================================================================================================================================================================================================

# Update Contact
def Update_contact():
    organize_contact()
    #Get user contact they wish to update.
    contactName = input("Tulis nama kontak yang anda ingin perbaruhi: ").title()
    # Checks if its a alphabet or char.
    N = contactName[0] if contactName[0].isalpha() else '#'
    for i in yellow_pages[N]:
        if (contactName == i['nama']):
            changeName = input("Would you like to change the contact's name? (Y/N):  ").title()
            changeName_assurance = changeName[0]
            if changeName_assurance == "Y":
                i['nama'] = input("Please enter new Name: ").title()
            else:
                print('\n')
                print('Moving on to contact number.')
                print('\n')
            changeHp = input("Would you like to change the contact's hp? (Y/N):  ").title()
            changeHp_assurance = changeHp[0]
            if changeHp_assurance == "Y":
                i['hp'] = input("Please enter new Number: ")
            else:
                print('\n')
                print('Moving on to contact Kota.')
                print('\n')
            
            changeKota = input("Would you like to change the contact's Kota? (Y/N):  ").title()
            changeKota_assurance = changeKota[0]
            if changeKota_assurance == "Y":
                i['Kota'] = input("Please enter new Kota: ")
            else:
                print('\n')
                print('Moving on to contact zip.')
                print('\n')
            
            changeZip = input("Would you like to change the contact's Zip? (Y/N):  ").title()
            changeZip_assurance = changeZip[0]
            if changeZip_assurance == "Y":
                i['zip'] = input("Please enter new Zip: ")
            else:
                print('\n')
                print('Moving on to updating contact.')
                print('\n')
            
            print('\n')
            print('\n')
            print("Contact has been updated successfully")
            return
        else:
            print('\n')
            print("!!!<-----Contact not found----->!!!")
            print('\n')

# ==========================================================================================================================================================================================================
# Update Contact End 
# ==========================================================================================================================================================================================================

# ==========================================================================================================================================================================================================
# Delete Contact Start 
# ==========================================================================================================================================================================================================

# Delete contact
def Delete_contact():
    #prints current contact list for better reference
    organize_contact()
    # Ask user which contact they want to delete.
    contactName = input("Tulis nama kontak yang anda ingin hapus: ").title()
    # checks if the contact exsist.
    N = contactName[0] if contactName[0].isalpha() else '#'
    # iterates contact list to find a match
    # need to check if the contact exist first.
    contact_found = False
    
    if N in yellow_pages:
        contact_found = True
    else:
        print('\n')
        print("!!!<-----Kontak tidak ditemukan----->!!!")
        print('\n')
        print("Pulang kembali ke Menu Utama.")
        return

    if contact_found:    
        assurance = input("Anda yakin ingin menghapus kontak? (Y/N): ").title()
        if assurance == "Y":
            for i in yellow_pages[N]:
                if (contactName == i['nama']):
                    yellow_pages[N].remove(i)
                    print("kontak berhasil dihapus.")
                    return
        elif assurance =="N":
            print('\n')
            print("Baik kita akan pelung balik ke Menu Utama.")
        else:
            print('\n')
            print("Input yang salah. Program ini akan kembali ke menu utam.")

# ==========================================================================================================================================================================================================
# Delete Contact End 
# ==========================================================================================================================================================================================================


# Find user by alphabet, name or just list everything at once.
def organize_options():
    
    state = True
    while state:
        print('''
    How would you prefer retrieve your desired contact.
    1. Semua Kontak yang di hurai.
    2. guna huruf.
    3. guna Nama kontak.
    4. Keluar.
    ''') 
        userOption = input("Input dari 1 - 4: ")
        if userOption == "1":
            print(' ')
            print("Kontak List:- ")
            # organize the alphabets
            organized = dict(sorted(yellow_pages.items()))
            #Organize the dictionary of the alphabets
            for i in organized:
            #use sorted based on keys
                organized[i]= sorted(yellow_pages[i], key=lambda d: d['nama'])
                # If new key is added and empty it skips it.
                if len(organized[i]) > 0:
                    print(i)
                else:
                    continue
                for j in organized[i]:
                    print('  ', j['nama'],'\n','|',"contact: ", j['hp']," "*(15 -len(j['hp'])), "|", "kota: ", j['kota']," "*(15 -len(j['kota'])), "|" ,"zip: ", j['zip']," "*(7 -len(j['zip'])), "|")
                    print('--------------------------------------------------------------------------')
                print()
            print('^^^ Scroll Atas ^^^')
            
        elif userOption == "2":
            contactAlph = input('Huruf apa anda mahu check? ').title()
            N = contactAlph[0] if contactAlph[0].isalpha() else '#'
            count = 0 
            print('\n ')
            print(f"Kontak List dalam huruf {N}:- ")
            if yellow_pages.get(N) is not None:
                print(N)
                for i in yellow_pages[N]:
                    print('  ', i['nama'],'\n','|',"contact: ", i['hp']," "*(15 -len(i['hp'])), "|", "kota: ", i['kota']," "*(15 -len(i['kota'])), "|" ,"zip: ", i['zip']," "*(7 -len(i['zip'])), "|")
                    print('--------------------------------------------------------------------------')
                    count += 1
                print('\n')
                print(f"Dalam tab huruf {N} ada {count} orang.")
            else:
                print('\n')
                print(f"Tiada orang dalam tab huruf {N}")
                print('\n')
                print('Balik ke cari Kontak Menu.')
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

# ==========================================================================================================================================================================================================
# Main Functions Start 
# ==========================================================================================================================================================================================================


# ==========================================================================================================================================================================================================
# Program script Start 
# ==========================================================================================================================================================================================================

# organize_contact()
Greeting()
while True:
    Menu()
    userOption = input(" Sila pilih nomor: ")
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

# ==========================================================================================================================================================================================================
# Program script Start 
# ==========================================================================================================================================================================================================
