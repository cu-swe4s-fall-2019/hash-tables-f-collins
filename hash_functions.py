import argparse

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

def h_rolling(key, N, p=53, m=2**64):
    key = str(key)

    if len(key) == 0:
        return 0
    if N <= 0:
        return None

    s = 0
    for i in range(len(key)):
        s += ord(key[i]) * p ** i

    s = s % m
    return s % N


def main():
    parser = argparse.ArgumentParser(description='Hash Functions.',
                                     prog='hashfunctions')

    parser.add_argument('--input_file',
                        type=str,
                        help='The file containing a set of input data.',
                        required=True)

    parser.add_argument('--hash_function',
                        type=str,
                        help='The hash function, either ascii or rolling.',
                        required=True)

    parser.add_argument('--table_size',
                        type=str,
                        help='The size of the hash table.',
                        required=True)
    
    args = parser.parse_args()

    infile = open(args.input_file, "r")

    if args.hash_function == "ascii":
        hash_function = h_ascii
    elif args.hash_function == "rolling":
        hash_function = h_rolling
    else:
        sys.exit(1)

    for line in infile:
        print(hash_function(line, int(args.table_size)))


if __name__ == "__main__":
    main()
