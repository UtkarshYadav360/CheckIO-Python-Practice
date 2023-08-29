# EXERCISE 19 :
# write a function that takes a text, and return the text in correct form with first letter capital and the text should end with '.'


def correct_text(text: str):
    """Takes text and return it in such a format, with first letter capital and ends with a full stop."""
    return text[0].upper() + text[1:] + ("." if text[-1] != "." else "")


text = input("Enter a sentence : ")

output = correct_text(text)

print(f"Corrected Text :\n{output}")
