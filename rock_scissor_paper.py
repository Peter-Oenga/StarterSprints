from cryptography.fernet import Fernet

master_pwd = input("What is your password? ")
def write_key():
    key = Fernet.generate_key()
    with open("key,key", "wb") as key_file:
        key_file.write(key)

def view():
    with open("password.txt", 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, pwd = data.split("|")
            print("Username:", user, ", Password:", pwd)


def add():
    name = input("Account name: ")
    password = input("Password ")
    with open("password.txt", 'a') as f:
        f.write(name + "|" + password + "\n")

mode = input("What is your mode (view, add) or enter Q to quit? ").lower()
while True:
    if mode == "q":
        break
    if mode == 'view':
        view()
        break
    elif mode == 'add':
        add()
        break
    else:
        print("Invalid input!")
        break

