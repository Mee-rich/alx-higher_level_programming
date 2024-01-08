#!/usr/bin/pyhton3
def replace_in_list(my_list, idx, element):
    if idx == -1:
        return None
    if idx not in range(len(my_list)):
        return None
    
    my_list[idx] = element
    return my_list


