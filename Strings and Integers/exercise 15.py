# EXERCISE 15 :
# write a function that takes a integer number and return the biggest digit from that number.


def max_digit(number: int):
    """Takes a integer number and return the biggest digit of that number."""
    return int(max(str(number)))


number = int(input("Enter a number : "))

output = max_digit(number)
print(f"{output} is the biggest number.")
