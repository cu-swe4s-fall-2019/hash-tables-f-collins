
def h_ascii(key, N):
    key = str(key)
    # We default to a hash of zero for empty strs so we can still store
    # empty strings
    if len(key) == 0:
        return 0
    if N <= 0:
        return None

    asciisum = 0
    for char in key:
        asciisum += ord(char)

    return asciisum % N

def h_rolling(key, N):
    return None
