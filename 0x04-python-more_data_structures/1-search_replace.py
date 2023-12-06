#!/usr/bin/python3

def search_replace(my_list, search, replace):
    new_list = []

    for item in my_list:
        new_element = replace if item == search else item
        new_list.append(new_element)

    return new_list
