

# [1, 2, 3, 4] -> iterable

l = [1, 2, 3]

# next(l)


iter_l = iter(l)

print(iter_l)

print(next(iter_l))
print(next(iter_l))
print(next(iter_l))


class Iterator:

    def __init__(self):
        # self.db = db
        self.current = 0


    def __iter__(self):
        pass

    def __next__(self):
        if len(self.db.filter()) > 10:
            return self.current + 10







