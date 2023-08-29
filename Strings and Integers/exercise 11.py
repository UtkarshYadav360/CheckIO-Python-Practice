# EXERCISE 11 :
# write a function that takes password and return True if it has more than 6 characters, and contains letters and numbers, but if the password is greater than 9 characters then the previous rule cannot apply, else return False.


def is_acceptable_password(password: str):
    """Takes passord and return True it has more than 6 characters with numbers and letters, but if it has more than 9 characters then no special condition is checked, else return False."""
    return (
        len(password) > 6
        and any(char.isdigit() for char in password)
        and any(char.isalpha() for char in password)
        or len(password) > 9
    )


password = input("Enter your password : ")

output = is_acceptable_password(password)

if output:
    print(f"{password} is a valid password.")
else:
    print(f"{password} is not a valid password.")
