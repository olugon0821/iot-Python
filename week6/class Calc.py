class Calculator:
    def plus (self, a, b):
        return a + b
    def minus (self, a, b):
        return a - b
    def multiple (self, a, b):
        return a * b
    def divide (self, a, b):
        if b == 0:
            print('You can not divide')
        return a / b
    
if __name__ == "__main__":
        
    cal = Calculator()
        
    a = 10
    b = 5
        
    print(f'{a} + {b} = {cal.plus(a,b)}')
