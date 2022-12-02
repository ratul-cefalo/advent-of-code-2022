'''
Day 1
'''
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
    heappush(calorie_sum_list,total)
    total = 0

# puzzle 1
ic(max_calorie)

#puzzle 2
ic(sum(nlargest(3,calorie_sum_list)))
