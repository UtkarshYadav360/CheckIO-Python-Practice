# EXERCISE 22 :
# write a function that takes a number, and return how many 0's are at the end of the number.


def check_number(number: int):
    """Takes a number and return the number of 0's at the end of the number."""
    str_number = str(number)
    return len(str_number) - len(str_number.rstrip("0"))


number = int(input("Enter a number : "))

ouptut = check_number(number)
print(ouptut)
