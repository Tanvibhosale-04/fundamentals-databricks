
from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity):
        self.cap = capacity
        self.data = OrderedDict()

    def get(self, key):

        if key not in self.data:
            return None

        self.data.move_to_end(key)

        return self.data[key]

    def put(self, key, value):

        if key in self.data:
            self.data.move_to_end(key)

        elif len(self.data) >= self.cap:
            self.data.popitem(last=False)

        self.data[key] = value


if __name__ == "__main__":

    cache = LRUCache(3)

    cache.put(1, 100)
    cache.put(2, 200)
    cache.put(3, 300)

    print(cache.get(1))

    cache.put(4, 400)

    print(cache.get(2))
    print(cache.get(3))
    print(cache.get(4))
