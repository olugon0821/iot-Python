class Circle :
    def __init__ (self, r):
        r = self.r
        self.pi = 3.14159
        
    def Area (self):
        return self.pi*(self.r**2)
    
    def circum (self):
        return 2*self.pi*self.r


    def toString(self):
        return "넓이 : {}\n둘레 : {}".format(self.getArea(),self.getcircum())


Circle = Circle(float(input("반지름을 입력하세요 : ")))
print(Circle.toString())
