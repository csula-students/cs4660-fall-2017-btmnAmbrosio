class List(object):
    def __init__(self):
        self.memory = []
        # we store the length separately because in real life
        # the "memory" doesn't have a length you can read from
        self.length = 0

    def get(self, address):
        return self.memory[address]

    def push(self, value):
        self.memory.insert(self.length, value)
        self.length += 1

    def pop(self):
        if self.length == 0:
            return

        lastAddress = self.length - 1
        value = self.memory[lastAddress]
        del self.memory[lastAddress]
        self.length -= 1

        return value

    def unshift(self, value):
        # push item to beginning of the list
        previous = value

        # use enumerate to loop with index (address)
        for address, _ in enumerate(self.memory):
            current = self.memory[address]
            self.memory[address] = previous
            previous = current

        self.memory.insert(self.length, previous)
        self.length += 1

    def shift(self):
        # pop first item out of list
        if self.length == 0:
            return

        value = self.memory[0]

        # use enumerate to loop with index (address)
        for address, _ in enumerate(self.memory):
            self.memory[address] = self.memory[address + 1]

        del self.memory[self.length - 1]
        self.length -= 1

        return value

class HashTable(object):
    def __init__(self):
        self.memory = {}

    def hashKey(self, key):
        hash_token = 0
        for character in key:
            hash_token = 101 * hash_token + ord(character)
        return hash_token

    def get(self, key):
        address = self.hashKey(key)
        return self.memory[address]

    def set(self, key, value):
        address = self.hashKey(key)
        self.memory[address] = value

    def remove(self, key):
        address = self.hashKey(key)
        if address in self.memory:
            del self.memory[address]
