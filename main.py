def ypr1():
    x = int(input('Введите число: '))
    y = [3, 5, 17, 99, 67]
    if x in y:
        print("Вот загаданные числа: ", y, '\n', "Вот твое число: ", x, '\n', 'Молодец! Ты угадал число')
    else:
        print("Вот загаданные числа: ", y, '\n', "Вот твое число: ", x, '\n', 'Упс. Ты не угадал число')

ypr1()

def ypr2():
    slovo = ['солнце', 'дождь', 'гроза', 'солнце']
    povtor = {str(x) for x in slovo if slovo.count(x) > 1}
    x = lambda: print('nothing')
    y = lambda: print(' '.join(povtor))
    x() if len(povtor) < 1 else y()

ypr2()

def ypr3():
    week = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sun', 'Sut')
    weekends = int(input())
    print('Weekends:', week[:-weekends - 1:-1])
    print('Work days:', week[:-weekends])

ypr3()

def ypr4():
    f1 = ['Кузнецова', 'Венцель', 'Мостовая']
    f2 = ['Крипилина', 'Лободедова', 'Стомина']
    sport = (f1[0], f2[1], f2[2])
    print(*f1)
    print(*f2)
    print(*sport)
    print(len(sport))
    sport = tuple(sorted(sport))
    print(sport)
    if 'Кузнецова' in sport:
        print("Кузнецова есть в команде")

ypr4()

