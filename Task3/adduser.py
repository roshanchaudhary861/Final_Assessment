def adduser():
    username = input("Enter the username:  ")
    realname = input("Enter the real name: ")
    password = input("Enter the password:  ")
    with open("passwd.txt", "r+") as f:
        for line in f:
            if username == line.split(":")[0]:
                print("Cannot add. Most likely username already exists.")
                print("```")
                return
        f.write(f"{username}:{realname}:{password}\n")
        print("User Created.")
        
        
        
adduser()      