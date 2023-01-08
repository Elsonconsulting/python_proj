def register():
    db = open("C:\Python Projects\database.txt", "r")
    Username = input("Create username: ")
    if Username in db:
       print("Username already exist")
    register()
    Password_ini = input("Create password: ")
    Password = input("Confirm password: ")

    if len(Password)<=6:
        print("Password too short")
        register()
    if len(Password)>=13:
        print("Password too long")
        register()
    if Password != Password_ini:
        print("Confirmed password did not match, try again")
    pass

register()

def access():
    pass