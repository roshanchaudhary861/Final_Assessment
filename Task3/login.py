import getpass


def login():
    username = input("User:     ")
    password = getpass.getpass("Password: ")

    with open("passwd.txt", "r") as f:
        for line in f:
            # Split the line into fields using colon as the separator
            fields = line.strip().split(":")
            if len(fields) == 3:
                stored_username, stored_password = fields[0], fields[2]
                if username == stored_username and password == stored_password:
                    print("Access granted.")
                    return True
        print("Access denied.")
        return False

login()
