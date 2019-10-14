class Rectanle(object):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def perimeter(self):
        Per = self.length + self.width
        return Per
    def square(self):
        Sq = self.length * self.width
        return Sq

if __name__ == "__main__":
    rect = Rectanle(2,3)
    print(rect.perimeter())
    print(rect.square())