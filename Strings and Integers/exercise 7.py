# EXERCISE 7 :
# write a function that takes a non-negative number and returns how many digits the number have.


def number_length(num: int):
    """Takes a number and return the number of digits it have."""
    return len(str(num))


number = int(input("Enter a non-negative number : "))

output = number_length(number)
print(f"Your number has {output} digits.")
