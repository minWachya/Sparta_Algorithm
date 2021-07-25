class Dict:
    def __init__(self):
        self.itwms = [None] * 8

    def put(self, key, value):
        index = hash(key) % len(self.itwms)
        self.itwms[index] = value

    def get(self, key):
        index = hash(key) % len(self.itwms)
        return self.itwms[index]


my_dict = Dict()
my_dict.put("test", 3)
print(my_dict.get("test"))