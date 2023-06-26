#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    nb_print = 0
    try:
        for i in range(x):
            try:
                print(str(my_list[i]), end="")
                nb_print += 1
            except IndexError:
                pass
    except TypeError:
        pass
    finally:
        print("\n")
    return nb_print
