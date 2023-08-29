# EXERCISE 9 :
# write a function that takes a password as input as a string and return True if it have more than 6 characters and contains atleast one number, else return False.


def is_acceptable_password(password: str):
    """Take password and return True if the password has more than 6 characters and contains atleast one number, else return False."""
    return len(password) > 6 and any(char.isdigit() for char in password)


password = input("Enter your password : ")

output = is_acceptable_password(password)

if output:
    print(f"{password} is a valid password.")
else:
    print(f"{password} is not a valid password.")
