# Reverse a String

def reverseString(string):
    length = len(string)
    reverse_string = ""
    while length > 0:
        reverse_string += string[length-1:length]
        length -= 1
    return reverse_string
