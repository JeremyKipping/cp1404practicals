"""Jeremy Kipping"""

MIN_LENGTH = 4

def main():
    get_password()


def get_password():
    """Get a password from a user"""
    print("Please enter a password. It must be longer than 3 characters")
    password = input(">>>")
    check_password(password)

def check_password(password):
    password_check(password)





def password_check(password):
    """Check password from user"""
    if len(password) >= 4:
        for char in range(len(password) + 1):
            print('*')
        print()
    else:
        print("That password is an invalid length")
        print("Please enter a password. It must be longer than 3 characters")
        password = input(">>>")


main()
