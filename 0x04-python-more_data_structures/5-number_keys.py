#!/usr/bin/python3
def number_keys(a_dictionary):
    num = 0
    new_keys = list(a_dictionary.keys())

    for i in new_keys:
        num += 1

    return (num)
