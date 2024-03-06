import datetime

now = datetime.datetime.now()

month = int(input('월을 입력하세요>'))

if 3<= month <=5:
    print(f'{month}월달은 봄 입니다.')
    
if 6<= month <=8:
    print(f'{month}월달은 여름 입니다.')
    
if 9<= month <=11:
    print(f'{month}월달은 가을 입니다.')
    
if month == 12 or 1<= month <=2:
    print(f'{month}월달은 겨울 입니다.')
