class Numbers:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)


    def add(self):
        return (self.x + self.y)

num1 = input('Enter first number: ')
num2 = input('Enter second number: ')
summation = Numbers(num1, num2)

print('%s + %s = %s' %(summation.x, summation.y, summation.add()))