import json

# File path to store user data
USER_DATA_FILE = 'user_data.json'

def load_user_data():
    try:
        with open(USER_DATA_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_user_data(data):
    with open(USER_DATA_FILE, 'w') as file:
        json.dump(data, file)

def sign_up():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    user_data = load_user_data()

    if username in user_data:
        print("Username already exists. Please choose a different one.")
        return

    user_data[username] = {'password': password}
    save_user_data(user_data)
    print("Sign up successful!")

def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    user_data = load_user_data()

    if username not in user_data or user_data[username]['password'] != password:
        print("Invalid username or password. Please try again.")
    else:
        print(f"Welcome, {username}!")

# Main program loop
while True:
    print("\n1. Sign Up")
    print("2. Login")
    print("3. Quit")
    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        sign_up()
    elif choice == '2':
        login()
    elif choice == '3':
        break
    else:
        print("Invalid choice. Please try again.")
