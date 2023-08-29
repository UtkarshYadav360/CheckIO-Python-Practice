# EXERCISE 2 :
# write a function that takes a password as input as a string and return True if the passwod has more than 6 characters else return False.


def is_acceptable_password(password: str):
    """Takes password and return True if it has more than 6 characters."""
    return len(password) > 6


password = input("Enter your password : ")

output = is_acceptable_password(password)

if output:
    print(f"Your password has {len(password)} characters and it is acceptable.")
else:
    print(f"Your password has {len(password)} characters and it is not acceptable.")
