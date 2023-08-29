# EXERCISE 18 :
# write a function that takes a string of numbers only, and return the number of '0' at the beginning of the string.


def beginning_zeros(text: str):
    """Takes a string of numbers and return the count of '0' at the beginning of the string."""
    return len(text) - len(text.lstrip("0"))


text = input("Enter some digits : ")

output = beginning_zeros(text)

if output:
    print(f"There are {output} zeros in the beggining of your number.")
else:
    print("There are no zeros in the beggining of your number.")
