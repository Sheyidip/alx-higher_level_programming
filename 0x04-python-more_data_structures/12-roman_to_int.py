#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0
    roman_d = {'I': 1, 'v':5, 'x':10, 'L':50, 'c':100, 'D':500, 'M':1000}
    roman_n =0
    for j in range(len(roman_string)):
        if j > 0 and roman_d[roman_string[j]] > roman_d[roman_string[j - 1]]:
