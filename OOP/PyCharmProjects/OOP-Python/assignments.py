class MaxSizeList(object):
    def __init__(self, val):
        self.l = []
        self.listSize = val
    def push(self, el):
        self.l.append(el)
        if len(self.l) > self.listSize:
            self.l.pop(0)
    def get_list(self):
        return self.l

a = MaxSizeList(0)
b = MaxSizeList(0)

a.push("hey")
a.push("hi")
a.push("lets")
a.push("go")

b.push("hey")
b.push("hi")
b.push("lets")
b.push("go")

print(a.get_list())
print(b.get_list())
