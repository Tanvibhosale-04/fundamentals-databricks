
from collections import OrderedDict

class FIFOCache:

    def __init__(self, capacity):
        self.cap = capacity
        self.data = OrderedDict()

    def get(self, key):

        if key not in self.data:
            return None

        return self.data[key]

    def put(self, key, value):

        if key in self.data:
            self.data[key] = value

        else:
            if len(self.data) >= self.cap:
                self.data.popitem(last=False)

            self.data[key] = value


if __name__ == "__main__":

    cache = FIFOCache(3)

    cache.put(1, 100)
    cache.put(2, 200)
    cache.put(3, 300)

    print(cache.get(1))

    cache.put(4, 400)

    print(cache.get(1))
    print(cache.get(2))
    print(cache.get(4))
