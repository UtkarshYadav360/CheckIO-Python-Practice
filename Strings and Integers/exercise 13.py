# EXERCISE 13 :
# write a function that takes a string enclose within two different markers "<Hello>", and return the string between the markers there can't be more than one marker on each side.


def between_markers(text: str, start: str, end: str):
    """Takes text, start argument and end argument and return the text within the markers."""
    start_position = text.find(start) + 1
    end_position = text.find(end)
    return text[start_position:end_position]


text = input("Enter some text : ")
start = input("Enter the first marker : ")
end = input("Enter the second marker : ")

output = between_markers(text, start, end)

if output:
    print(f"Your text is {output}")
else:
    print("The markers you entered are incorrect.")
