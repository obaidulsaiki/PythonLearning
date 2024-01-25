from cryptography.fernet import Fernet

def writing_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def loading_key():
    return open("key.key", "rb").read()

writing_key()
key = loading_key()
Fer = Fernet(key)
MasterPass = input("Enter the master password: ")

if MasterPass == "1234":
    while True:
        print("Options:")
        print("1. Add a new password a")
        print("2. View password v")
        print("3. Exit the program press q")
        mode = input("Enter a mode: ")
        if mode == "q":
            break
        elif mode == "a":
            name = input("Account Name: ")
            password = input("Enter a new password: ")
            encrypted_password = Fer.encrypt(password.encode()).decode()
            with open("passwords.txt", "a") as password_file:
                password_file.write(name + " " + encrypted_password + "\n")
        elif mode == "v":
            with open("passwords.txt", "r") as password_file:
                for line in password_file.readlines():
                    name, encrypted_password = line.strip().split(" ")
                    decrypted_password = Fer.decrypt(encrypted_password.encode()).decode()
                    print(f"The Account {name} has the password: {decrypted_password}")
        else:
            print("Invalid mode.")
else:
    print("Wrong password")
    exit()
