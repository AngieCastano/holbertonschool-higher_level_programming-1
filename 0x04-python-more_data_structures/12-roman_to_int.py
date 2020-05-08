#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None:
        return 0
    nums = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    for i in roman_string:
        if i not in nums:
            return 0
    prev = nums.get(roman_string[0])
    for j in roman_string:
        num = nums.get(j)
        if prev >= num:
            result += num
        elif prev < num:
            result = result + num - prev - prev
        prev = num
    return result
