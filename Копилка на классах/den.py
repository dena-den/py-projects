class MoneyBox:
    def __init__(self, capacity):
        self.capacity=capacity
        self.count=0
        print('Box created with ', self.capacity, ' capacity.')

    def can_add(self, v):
        if self.capacity>=self.count+v:
            print('Yes, you can')
            return True
        print('No, you cant')
        return False

    def add(self, v):
        if self.can_add(v):
            self.count+=v
            print('New count: ',self.count)
        print('Too much')

a=MoneyBox(10)
a.can_add(5)
a.add(12)
a.add(9)
a.can_add(3)