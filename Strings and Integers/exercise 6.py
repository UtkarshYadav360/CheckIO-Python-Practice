# EXERCISE 6 :
# write a function that takes a string and return the first word of the string. The string can contain alphabets and spaces.


def first_word(text: str):
    """Takes a text and return the first word of the text."""
    split_text = text.split(" ")
    return split_text[0]


text = input("Enter some text : ")

output = first_word(text)
print(f"Your first word is {output}")
