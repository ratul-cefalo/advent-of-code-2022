from cc_input import given_cases

contained_count = 0
overlap_count = 0
for elf1, elf2 in given_cases:
    if elf1.intersection(elf2):
        overlap_count += 1
        if elf1.issubset(elf2) or elf1.issuperset(elf2):
            contained_count += 1

assert contained_count == 644
assert overlap_count == 926
