'''Given an integer x, return true if x is palindrome integer.'''

def ispolid(integer):
    tmp = str(integer)
    if tmp == tmp[::-1]:
        return True
    return False
