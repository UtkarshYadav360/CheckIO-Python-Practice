# EXERCSIE 10 :
# write a function that takes a password as input and return True if it has more than 6 characters and contain numbers and letters, else return False


def is_acceptable_password(password: str):
    """Takes password and return True if it has more than 6 characters and contains lettes and numbers both, else return False."""
    return (
        len(password) > 6
        and any(char.isdigit() for char in password)
        and any(char.isalpha() for char in password)
    )


password = input("Enter your password : ")

output = is_acceptable_password(password)

if output:
    print(f"{password} is a valid password.")
else:
    print(f"{password} is not a valid password.")
