# EXERCISE 1 :
# write a function that takes two integer numbers as input and return the product of these two numbers.


def multiply(a: int, b: int):
    """Takes two integers as input and return the product."""
    product = a * b
    return product


n1 = int(input("Enter the first number : "))
n2 = int(input("Enter the second number : "))

output = multiply(n1, n2)
print(f"The product of your numbers is {output}.")
