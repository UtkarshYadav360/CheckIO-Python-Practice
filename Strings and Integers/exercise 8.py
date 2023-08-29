# EXERCISE 8 :
# write a function that takes a number and return "Fizz" if it is divisible by 3, return "Buzz" if it is divisible by 5, return "Fizz Buzz" if it is divisible by 3 and 5 both, else return the number as a string.


def check_number(num: int):
    if num % 3 == 0 and num % 5 == 0:
        return "Fizz Buzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return str(num)


number = int(input("Enter a number : "))

output = check_number(number)

if output.isnumeric():
    print(f"{output} {type(output)}")
else:
    print(output)
