#!/usr/bin/python3

def best_score(a_dictionary):
    max_score = 0
    best_score = None
    if a_dictionary:
        for key in a_dictionary:
            value = a_dictionary[key]
            if value > max_score:
                max_score = value
                best_score = key
        return best_score
    return None
