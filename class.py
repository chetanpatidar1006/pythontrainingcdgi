class Abc:
    def __init__(self, x, y):
        self.b = x
        self.a = x

    def bcd(self):
        nums = [1, 2, 3, 4, 5, 6, 7, 9, 10, 11]
        for num in nums:
            print(str(num))



x = Abc(2.2, -23)
print(x.a, x.b)
x.bcd()
