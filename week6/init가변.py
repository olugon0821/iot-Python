class Book:
    def __init__(self,*args):
        if len(args) == 1:
            self.name = args[0]
            self.year = ''
        elif len(args) == 2:
            self.name = args[0]
            self.year = args[1]


if __name__ == "__main__":
    s1 = Book("파이썬")
    s2 = Book("ai",2024)
    print(s1.name,s1.year)
    print(s2.name,s2.year)
