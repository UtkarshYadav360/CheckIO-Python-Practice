# EXERCISE 12 :
# write a function that takes password and return True if the password has more than 6 characters and contains numbers and letters, but if the password has more than 9 letters than the previous rule cannot apply, and the word "password" cannot be used in the password in any case.


def is_acceptable_password(password: str):
    """Takes password and return True if the password has more than 6 characters with numbers and letters, but if it has more than 9 characters then no special condition is checked, return False if there is "password" in the password."""
    if "password" in password.lower():
        return False
    elif (
        len(password) > 6
        and any(char.isdigit() for char in password)
        and any(char.isalpha() for char in password)
        or len(password) > 9
    ):
        return True
    else:
        return False


password = input("Enter your password : ")

output = is_acceptable_password(password)

if output:
    print(f"{password} is a valid password.")
else:
    print(f"{password} is not a valid password.")
