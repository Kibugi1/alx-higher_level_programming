#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = []
    add = 0
    for numb in my_list:
        if numb not in new_list:
            add = add + numb
            new_list.append(numb)
    return add
