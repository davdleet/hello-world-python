class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def setdata(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        result = self.first + self.second
        print(result)

    def mul(self):
        result = self.first * self.second
        print(result)

    def sub(self):
        result = self.first - self.second
        print(result)

    def div(self):
        result = self.first / self.second
        print(result)


class Morefour(FourCal):
    def pow(self):
        result = self.first ** self.second
        print(result)


class SafeFourCal(FourCal):
    def div(self):
        if self.second == 0:
            print(0)
        else:
            result = self.first / self.second
            print(result)


a = SafeFourCal(4, 0)
a.div()

