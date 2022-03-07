'''
Created on 3/7/2022

@author: estuche77
'''


def TryConvertPositiveInteger(string_value):
    try:
        integer = int(string_value)
        if (integer <= 0):
            return False, 0
    except ValueError:
        return False, 0

    return True, integer
