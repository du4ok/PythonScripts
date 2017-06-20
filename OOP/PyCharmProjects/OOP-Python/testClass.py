class InstanceCounter(object):
    count = 0

    def __init__(self, val):
        self.val = self.filterint(val)
        InstanceCounter.count += 1

    @staticmethod
    def filterint(value):
        if not isinstance(value, int):
            return 0
        else:
            return value

    @classmethod
    def get_count(cls):
        return cls.count

a = InstanceCounter(5)
b = InstanceCounter("aaa")
c = InstanceCounter(15)

print(a.val)
print(b.val)
print(c.val)
print(a.get_count())