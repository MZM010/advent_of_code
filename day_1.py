#!/usr/bin/python3
import re

def contains_single_digit_number(string):
    pattern = r"\b\d\b"
    match = re.search(pattern, string)
    if match:
        return True
    else:
        return False

def return_the_sum(string):
    long_arr = []
    counter = 0
    for line in string:
        small_string = ""
        for i in range(len(line)):
            if line[i].isdigit():
                small_string += line[i]
        if small_string:
            two_digit_value = small_string[0] + small_string[-1]
            long_arr.append(two_digit_value)
        print(long_arr)
    for i in long_arr:
        counter += int(i)
    return counter


file = open("input.txt", "r")
splited_line = file.read().splitlines()
calibration_sum = return_the_sum(splited_line)
print(calibration_sum)
