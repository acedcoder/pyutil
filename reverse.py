def reverse(value):
    "Reverses an iterable sequence or returns None"
    if (type(value) == str):
        valLen = len(value)
        return value[valLen:-valLen - 1:-1]
    elif (type(value) == list or type(value) == tuple):
        return value[::-1]
    else:
        return "Cannot reverse argument."