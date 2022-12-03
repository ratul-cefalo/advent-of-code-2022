from icecream import ic
from puzzle_input import given_cases
import string

char_values = {
    letter: values for values, letter in (enumerate(string.ascii_letters, start=1))
}

# puzzle 1
sum = 0
for item in given_cases:
    half_point = len(item) // 2
    firstpart, secondpart = map(set, (item[:half_point], item[half_point:]))
    common_letter = firstpart & secondpart
    sum += char_values[common_letter.pop()]

assert sum == 8105

# puzzle 2
sum = 0
for i in range(0, 299, 3):  #  start, stop, step
    first, second, third = map(set, given_cases[i : i + 3])
    common_character = first & second & third
    sum += char_values[common_character.pop()]

assert sum == 2363
