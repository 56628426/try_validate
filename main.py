print("Welcome to JoppersDEV platform")
print("")
print("1. Register")
print("2. Login")

choice = input('Select your option {1-2}:')
if choice == "1":
    def register():
        print("")
        print('registering')
        global names
        global contacts
        global emails
        global country
        global district
        global age
        names = str(input('Enter your name:'))
        contacts =int(input('Enter your contact number:'))
        emails = str(input('Enter your email:'))
        country = str(input('Enter your country name:'))
        district = str(input('Enter your district:'))
        age = int(input('Enter your age:'))
        print(f'{names} thank you for registerd please login')
        print("")
    register()
choice = input('Enter 2 to login:')
if choice == "2":
    def login():
        print("")
        print('login form')
        name = str(input('Enter your name:'))
        email = str(input('Enter your email:'))

        if name in names:
            print(f'{names} : your name is verifyed')
        if email in emails:
            print(f'{emails} : your email is verifyed')
            print("")
            print('Getting access now opperate your account')
        else:
            print('Ooooopss, Please try again')
            register()
            login()
            results()
            proceed()
    login()
choice = input('Enter 3 to show your profile:')
if choice == "3":
    def results():
        print("")
        print(f'Name :{names}')
        print(f'Contact :{contacts}')
        print(f'Email :{emails}')
        print(f'Country :{country}')
        print(f'District :{district}')
        print(f'Age :{age}')
    results()
choice = input('4 to continue / 5 to edit profile:')
if choice == "4":
    def proceed():
     while True:
        print('CONGORATURATION')
    proceed()

if choice == "5":
    def edit():
        print("")
        print('Edit your profile')
        register()
        login()
        results()
        proceed()
    edit()
else:
    print("ooooops who is you?")
