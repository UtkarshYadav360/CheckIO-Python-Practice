# EXERCISE 3 :
# write a function that takes a number and return True if it is even else return odd.


def is_even(num: int):
    """Takes a number and return True if the number is even else return False."""
    return num % 2 == 0


number = int(input("Enter a number : "))

output = is_even(number)

if output:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")
