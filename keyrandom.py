import random


class Randomizer:
    def __init__(self, chars: str, seed=None):
        self.chars = chars.replace(" ", "").split(",")
        self.rand = random.Random(seed)

    def set_chars(self, chars):
        self.chars = chars.replace(" ", "").split(",")

    def generate(self, key_length: int, seed=None):
        key = ""
        self.rand.seed(seed)
        for _ in range(key_length):
            key += self.chars[self.rand.randrange(0, len(self.chars))]
        return key

    def batch_generate(self, generation, key_length):
        keys = []
        for _ in range(generation):
            keys.append(self.generate(key_length))
        return keys
