# EXERCISE 16 :
# write a function that takes a string consist of letters and numbers and return the sum of the numbers in the string. Apart from the numbers that are joined with letters.


def sum_numbers(text: str):
    """Takes a string of letters and numbers and return the sum of those numbers that are seperated by spaces."""
    return sum(int(chars) for chars in text.split() if chars.isdigit())


text = input("Enter some text with letters and numbers : ")

output = sum_numbers(text)

print(f"Sum of the numbers that are present in your text is {output}.")
