class countdown_iterator:
    def __init__(self,count):
        self.count = count+1
        self.finish = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count == self.finish:
            raise StopIteration

        self.count -= 1
        return self.count

iterator = countdown_iterator(0)
for item in iterator:
    print(item, end=" ")
