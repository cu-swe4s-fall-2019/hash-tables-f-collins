from hash_functions import h_ascii, h_rolling

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


