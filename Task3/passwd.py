
import getpass
def passwd():
    username = input("User:             ")
    current_password = ("Current Password: ")
    new_password = getpass.getpass("New Password:     ")
    new_password_confirm = getpass.getpass("Confirm:          ")

    if new_password != new_password_confirm:
        print("Sorry, Passwords do not match")
        return

    with open("passwd.txt", "r") as f:
        lines = f.readlines()

    with open("passwd.txt", "w") as f:
        changed = False
        for line in lines:
            stored_username, stored_real_name, stored_password = line.strip().split(":")
            if username == stored_username and current_password ==(stored_password):
                f.write(f"{username}:{stored_real_name}:{new_password}\n")
                changed = True
                print("Password changed.")
            else:
                f.write(line)

        if not changed:
            print(" User not found or incorrect password.")

passwd()
