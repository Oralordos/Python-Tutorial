class Bag:
    def __init__(self, first):
        self.first = first
        self.items = []

    def __getitem__(self, index):
        if index == 0:
            return self.first
        else:
            return self.items[index-1]

    def __setitem__(self, index, value):
        if index == 0:
            self.first = value
        else:
            self.items[index-1] = value

    def add(self, item):
        self.items.append(item)

    def __len__(self):
        return len(self.items) + 1

    def __str__(self):
        v = str(self.first)
        for i in self.items:
            v += ', {}'.format(i)
        return v

b = Bag('hi')
b.add('test')
b.add('food')

print(b[0])

print(len(b))
print(b)
for i in b:
    print(i)
