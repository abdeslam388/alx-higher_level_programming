#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):

    counter = 0
    for y in range(0, x):
        try:
            print("{:d}".format(my_list[y]), end="")
            counter += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (counter)
