# EXERCISE 14 :
# write a function that takes word, first letter and second letter from that word and returns True if the second word just comes after the second word.


def goes_after(word: str, first_letter: str, second_letter: str):
    """Takes word, first letter and second letter from that word and check if the second letter comes after the first letter and return True."""
    first_word_position = word.find(first_letter)
    second_word_position = word.find(second_letter)
    return second_word_position - first_word_position == 1
    # return f"{first_letter}{second_letter}" in word  # ALTERNATIVE CODE, MORE OPTIMIZED


word = input("Enter your word : ")
first_letter = input("Enter a letter from the word : ").lower()
second_letter = input("Enter another letter from the word : ").lower()

output = goes_after(word, first_letter, second_letter)

if output:
    print(f"In '{word}', '{second_letter}' just comes right after '{first_letter}'")
else:
    print(f"In '{word}', '{second_letter}' doesn't comes right after '{first_letter}'")
