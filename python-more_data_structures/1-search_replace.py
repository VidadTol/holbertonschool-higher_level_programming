#!/usr/bin/python3

def search_replace(my_list, search, replace):
# Si num est égal à search, il est remplacé par replace.Sinon, num reste inchangé
    return [replace if num == search else num for num in my_list]
