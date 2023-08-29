# EXERCISE 5 :
# write a function that takes a positive integer and return "Fizz" if the number is divisible by 3, esle convert it to a string.


def check_number(num: int):
    """Takes a number and return 'Fizz' if it is divisible by 3 else return the number as a string."""
    return "Fizz" if num % 3 == 0 else str(num)


number = int(input("Enter a number : "))

output = check_number(number)

if output != "Fizz":
    print(f"{output} {type(output)}")
else:
    print("Fizz")
