def main():
    user_data = {}  # Store user info here

    while True:
        print("Welcome to JoppersDEV platform")
        print("1. Register")
        print("2. Login")
        print("3. Show profile")
        print("4. Continue")
        print("5. Edit profile")
        print("6. Exit")
        choice = input("Select your option (1-6): ")

        if choice == "1":
            def register():
                print("\nRegistering")
                user_data['name'] = input('Enter your name: ')
                user_data['contact'] = int(input('Enter your contact number: '))
                user_data['email'] = input('Enter your email: ')
                user_data['country'] = input('Enter your country: ')
                user_data['district'] = input('Enter your district: ')
                user_data['age'] = int(input('Enter your age: '))
                print(f"{user_data['name']}, thank you for registering. Please login.")

            register()

        elif choice == "2":
            def login():
                if not user_data:
                    print("Please register first.")
                    return
                print("\nLogin form")
                name = input('Enter your name: ')
                email = input('Enter your email: ')
                if name == user_data.get('name') and email == user_data.get('email'):
                    print(f"{name}, your details are verified.")
                else:
                    print("Incorrect details. Please try again or register.")
            login()

        elif choice == "3":
            def results():
                if user_data:
                    print("\nYour Profile:")
                    print(f"Name: {user_data.get('name', 'N/A')}")
                    print(f"Contact: {user_data.get('contact', 'N/A')}")
                    print(f"Email: {user_data.get('email', 'N/A')}")
                    print(f"Country: {user_data.get('country', 'N/A')}")
                    print(f"District: {user_data.get('district', 'N/A')}")
                    print(f"Age: {user_data.get('age', 'N/A')}")
                else:
                    print("No profile data found. Please register first.")
            results()

        elif choice == "4":
            print("Continuing... (Placeholder for further actions)")

        elif choice == "5":
            def edit():
                print("\nEdit your profile")
                register()
                print("Profile updated.")
            edit()

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
