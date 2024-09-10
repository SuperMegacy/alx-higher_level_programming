#!/usr/bin/python3
def uppercase(str):
    res = ""
    for ch in str:
        if 'a' <= ch <= 'z':
            res += chr(ord(ch) - 32)
        else:
            res += ch
    return(res)
