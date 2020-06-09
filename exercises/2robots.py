class Robot:

    def __init__(self, name=None):
        self.name = name

    def say_hi(self):
        if self.name:
            print("Hi, my name is " + self.name)
        else:
            print("Hi, I don't have name")

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name


x = Robot()
x.say_hi()
print(x.get_name())
x.set_name("Jimmy")
x.say_hi()
y = Robot("Arnold")
y.say_hi()
y.set_name(x.get_name())
y.say_hi()
print(y.get_name())
