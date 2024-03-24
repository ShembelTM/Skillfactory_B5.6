                #Приветсвие
def greet():
    print("-------------------")
    print("  Приветсвуем вас  ")
    print("      в игре       ")
    print("  крестики-нолики  ")
    print("-------------------")
    print(" формат ввода: х у ")
    print(" х - номер строки  ")
    print(" у - номер столбца ")
greet()
                #Приветсвие

field = [[" "] * 3 for i in range(3) ]

                #Вывод поля в консоль
def show():
    print()
    print("    | 0 | 1 | 2 | ")
    print("  --------------- ")
    for i, row in enumerate(field):
        row_str = f"  {i} | {' | '.join(row)} | "
        print(row_str)
        print("  --------------- ")
    print()
                #Вывод поля в консоль

                #Ход игрока
def ask():
    while True:
        cords = input("          Ваш ход: ").split()

        if len(cords) != 2:
            print("Введите 2 координаты!")
            continue

        x,y = cords

        if not(x.isdigit()) or not(y.isdigit()):
            print("Введите числа!")
            continue
        x,y = int(x), int(y)

        if 0 > x or x > 2 or 0 > y or y > 2:
            print("Координаты вне диапазона!")
            continue

        if field[x][y] != " ":
            print("Клетка занята!")
            continue

        return x,y
                #Ход игрока

                #Выйграшные комбинации
def check_win():
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win_cord:
        symbols = []
        for c in cord:
            symbols.append(field[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            print("Выйграл Х!")
            return True
        if symbols == ["0", "0", "0"]:
            print("Выйграл 0!")
            return True
    return False
                #Выйграшные комбинации

                #Очередность хода
num = 0
while True:
    num += 1
    show()

    if num % 2 == 1:
        print("Ходить крестик!")
    else:
        print("Ходить нолик!")

    x,y = ask()

    if num % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "0"

    if check_win():
        break
    if num == 9:
        break
        print("Ничья!")
                #Очередность хода

