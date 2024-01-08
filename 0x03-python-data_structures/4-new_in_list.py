#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    cpy_list = my_list[:]

    if idx == -1:
        return (cpy_list)
    
    if idx > (len(my_list)):
        return (my_list)

    if 0 <= idx < len(my_list):
        cpy_list[idx] = element
    
    return cpy_list
