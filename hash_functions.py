
def h_ascii(key, N):
    asciisum = 0
    for char in key:
        asciisum += ord(char)
    return asciisum % N

def h_rolling(key, N):
    return None
