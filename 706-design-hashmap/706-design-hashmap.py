class MyHashMap:

    def __init__(self):
        self.hmap= dict()

    def put(self, key: int, value: int) -> None:
        self.hmap[key]=value

    def get(self, key: int) -> int:
        if key in self.hmap:
            return self.hmap[key]
        else:
            return -1

    def remove(self, key: int) -> None:
        if key in self.hmap:
            self.hmap.pop(key)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)