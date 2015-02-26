__author__ = 'Administrator'
"""
len > = 10
1 digit
1 upper
1 lower

TODO: Make changes
"""
def checkio(data):
    length = False
    dig = False
    upp = False
    low = False

    length = len(data) >= 10
    for char in data:
        if(char.isdigit()):
            dig = True
        elif (char.isupper()):
            upp = True
        elif (char.islower()):
            low = True

    return length and dig and upp and low