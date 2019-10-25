from hash_functions import h_ascii, h_rolling
import argparse
import sys
import random
import time

class LinearProbe:
    def __init__(self, N, hash_function):
        self.hash_function = hash_function
        self.N = N

        self.L = [None] * self.N

    def add(self, key, value):
        start_hash = self.hash_function(key, self.N)

        try:
            while self.L[start_hash] != None:
                start_hash += 1
            self.L[start_hash] = (key, value)
            return 0
        except IndexError:
            return -1

    def search(self, key):
        start_hash = self.hash_function(key, self.N)
        for entry in self.L[start_hash:]:
            if key == entry[0]:
                return entry[1]
        return None

class ChainedHash:
    def __init__(self, N, hash_function):
        self.hash_function = hash_function
        self.N = N

        self.L = [[]] * self.N

    def add(self, key, value):
        start_hash = self.hash_function(key, self.N)

        self.L[start_hash].append((key, value))

    def search(self, key):
        start_hash = self.hash_function(key, self.N)
        for entry in self.L[start_hash]:
            if key == entry[0]:
                return entry[1]
        return None

def main():
    parser = argparse.ArgumentParser(description='Hash Tables.',
                                     prog='hashtables')

    parser.add_argument('--input_file',
                        type=str,
                        help='The file containing a set of input data.',
                        required=True)

    parser.add_argument('--hash_function',
                        type=str,
                        help='The hash function, either ascii or rolling.',
                        required=True)

    parser.add_argument('--hash_table',
                        type=str,
                        help='The hash table, either linear or chained.',
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

    if args.hash_table == "linear":
        hashtable = LinearProbe(int(args.table_size), hash_function)
    if args.hash_table == "chained":
        hashtable = ChainedHash(int(args.table_size), hash_function)

    prevtime = time.time()
    elements = 0
    for line in infile:
        elements += 1
        currenttime = time.time()
        hashtable.add(line, random.randint(0,1000))
        insertiontime = time.time() - currenttime
        print(str(elements/float(args.table_size)) + " " + str(insertiontime))

if __name__ == "__main__":
    main()
