"""
Day 1
"""
from heapq import heappush, nlargest
from calorie_counting_input import input_str
from icecream import ic

all_inputs = input_str.split("\n")

max_calorie = -1
calorie_sum_list = []
total = 0
for calorie in all_inputs:
    if calorie != "":
        total += int(calorie)
        continue
    max_calorie = max(total, max_calorie)
    heappush(calorie_sum_list, total)
    total = 0

if __name__ == "main":
    # puzzle 1
    assert max_calorie == 69795

    # puzzle 2
    assert sum(nlargest(3, calorie_sum_list)) == 208437
