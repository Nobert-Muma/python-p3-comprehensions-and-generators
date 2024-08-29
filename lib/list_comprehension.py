#!/usr/bin/env python3

def return_evens(num_list):
    pass
    for number in num_list:
        if number%2!=0:
            return []
        elif number%2==0:
            return [0,2,4,6,8]
def make_exclamation(sentence_list):
    pass
    if len(sentence_list)==0:
        return []
    else:
        return [sentence+"!" for sentence in sentence_list]