# EXERCISE 17 :
# write a function that takes a string as input with numbers and letters seperated by whitespaces, and return True if first three words are in succession.

# NOTE : numbers and alphabets cannot be combined together.


def has_three_words(text: str):
    """Takes string and returns True if it contains three words in succession."""
    words_count = 0
    for words in text.split():
        if words.isalpha():
            words_count += 1
        # words_count = (words_count + 1) * words.isalpha()  # ALTERNATIVE LINE FOR THE ABOVE IF CONDITION.
        if words_count == 3:
            return True
    else:
        return False


text = input(
    "Enter text with numbers and letters, where numbers and letters are not combined together : "
)

output = has_three_words(text)
print(output)
