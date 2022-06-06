#!/usr/bin/python3
def multiple_returns(sentence):
    lent = len(sentence)
    first_element = sentence[0] if lent > 0 else "None"
    tup = lent, first_element
    return(tup)
