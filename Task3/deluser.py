import getpass
def deluser():
    username = input("Enter username: ")
    with open("passwd.txt", "r") as f:
        lines = f.readlines()
    password = getpass.getpass("Enter password: ")    
    with open("passwd.txt", "w") as f:
        deleted = False
        for line in lines:
            if username == line.split(":")[0]:
                deleted = True
                continue
            f.write(line)
        if deleted:
            print("User Deleted.")
        else:
            print("sorry, User not found")
deluser()