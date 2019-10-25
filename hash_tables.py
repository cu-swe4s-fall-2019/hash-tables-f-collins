from hash_functions import h_ascii, h_rolling

class LinearProbe:
    def __init__(self, N, hash_function):
        self.hash_function = hash_function
        self.N = N

        self.L = [None] * self.N

    def add(self, key, value):
        start_hash = self.hash_function(key, self.N)
        print(start_hash)
        self.L[start_hash] = value

    def search(self, key):
        start_hash = self.hash_function(key, self.N)
        return self.L[start_hash]


class ChainedHash:
    def __init__(self, N, hash_function):
        self.hash_function = hash_function
        self.N = N

    def add(self, key, value):
        start_hash = self.hash_function(key, self.N)
        pass

    def search(self, key):
        start_hash = self.hash_function(key, self.N)
        pass


