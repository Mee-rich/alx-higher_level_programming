#!/usr/bin/python3
def no_c(my_string):
    mod_string= ''
    for i in my_string:
        if i != 'c' and i != 'C':
            mod_string += i
    return (mod_string)
        
