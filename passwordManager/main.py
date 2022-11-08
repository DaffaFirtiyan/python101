from cryptography.fernet import Fernet

# def writeKey():
#     key = Fernet.generate_key()
#     with open("passwordManager/key.key", "wb") as keyFile:
#         keyFile.write(key)

# writeKey()

def loadKey():
    with open("key.key", "rb").read() as file:
        key = file.read()
    return key

masterKey = input("Key: ")  
# append masterKey into the var
key = loadKey() + masterKey.encode()
fernet = Fernet(key)

def view():
    with open("passwordManager/passwords.txt", "r") as file:
        for i in file.readlines():
            data = i.rstrip()
            user, password = data.split("|")
            print(f"User: {user} - Password {fernet.decrypt(password.encode()).decode()}")

def add():
    name = input("Name: ")
    password = input("Password: ")

    with open("passwordManager/passwords.txt", "a") as file:
        file.write(name + "|" + str(fernet.encrypt(password.encode())) + "\n")

if __name__ == "__main__":
    while True:
        mode = input("(V)iew or (A)dd: ").lower()

        if mode == "q":
            break

        if mode == "v":
            view()
        elif mode == "a":
            add()