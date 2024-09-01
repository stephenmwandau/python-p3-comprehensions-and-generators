#!/usr/bin/env python3

def return_evens(num_list):
    evens = [num for num in num_list if num % 2 == 0]
    return evens  # This returns the list of even numbers, or an empty list if there are none

    pass

def make_exclamation(sentence_list):
    exclamations = [sentence + "!" for sentence in sentence_list]
    return exclamations  # This returns a list of sentences with exclamation marks added, or an empty list if input is empty

    pass