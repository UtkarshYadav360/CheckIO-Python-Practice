# EXERCISE 20 :
# write a function that takes a string and return the first word of that string.

# CRITERIA :
# There can be dots and commas in a string.
# A string can start with a letter or, for example, one/multiple dot(s) or space(s).
# A word can contain an apostrophe and it's a part of a word.
# The whole text can be represented with one word and that's it.


def first_word(text: str):
    """Takes a string and return the first word from it."""
    modified_text = text.replace(".", " ").replace(",", " ").split()
    return modified_text[0]


text = input("Enter some text that only contains lettes, spaces and dots : ")

output = first_word(text)

print(f"First Word : {output}")
