#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0

    for i in range(x):
        try:
            print("{}".format(my_list[i]), end='')
        except my_list is empty:
            break
        else:
            count += 1

    print()
    return (count)
