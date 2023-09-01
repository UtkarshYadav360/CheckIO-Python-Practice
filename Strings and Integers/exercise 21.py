# EXERCISE 21 :
# Stephen's speech module is broken. This module is responsible for his number pronunciation. He has to click to input all of the numerical digits in a figure, so when there are big numbers it can take him a long time. Help the robot to speak properly and increase his number processing speed by writing a new speech module for him. All the words in the string must be separated by exactly one space character. Be careful with spaces - it's hard to see if you place two spaces instead one.

FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

SECOND_TEN = [
    "ten",
    "eleven",
    "twelve",
    "thirteen",
    "fourteen",
    "fifteen",
    "sixteen",
    "seventeen",
    "eighteen",
    "nineteen",
]

OTHER_TENS = [
    "twenty",
    "thirty",
    "forty",
    "fifty",
    "sixty",
    "seventy",
    "eighty",
    "ninety",
]

HUNDRED = "hundred"


def new_speech_module(number: int):
    """Takes a integer number and return them in the alphabetical form , and words are sepreated only with one space. So the robot can speak them easily."""
    result = []
    # assert 0 < number < 1000, "number is out of supported range (1-999)"
    assert number > 0 and number < 1000, "number is out of supported range (1-999)"
    # if 100 <= number < 1000:
    if number >= 100 and number < 1000:
        result.append(FIRST_TEN[(number // 100) - 1])
        result.append(HUNDRED)
        number = number % 100
    # if 20 <= number <= 99:
    if number >= 20 and number <= 99:
        result.append(OTHER_TENS[(number // 10) - 2])
        number = number % 10
    # elif 10 <= number <= 19:
    elif number >= 10 and number <= 19:
        result.append(SECOND_TEN[number - 10])
        number = 0
    # if 1 <= number <= 9:
    if number >= 1 and number <= 9:
        result.append(FIRST_TEN[number - 1])
    return " ".join(result)


number = int(input("Enter a number (not more than 3 digits) : "))

output = new_speech_module(number)

print(output)
