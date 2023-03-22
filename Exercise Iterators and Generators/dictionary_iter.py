class dictionary_iter:
    def __init__(self,dictionary:dict):
        self.items = list(dictionary.items())
        self.iterations = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.iterations >= len(self.items) - 1:
            raise StopIteration
        self.iterations += 1

        return self.items[self.iterations]

result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
