# EXERCSIE 4 :
# write a function that takes a string and return it in the reverse order.


def reverse_string(chars: str):
    """Takes a string and return it in the reverse order."""
    return chars[::-1]


my_str = input("Enter something : ")

output = reverse_string(my_str)
print(f"Your reversed string is {output}.")
