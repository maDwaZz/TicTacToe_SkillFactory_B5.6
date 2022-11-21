import itertools # нам понадобится оператор cycle для переключения между игроками

def win(current_game):
    def all_same(l): # функция для определения условия выигрыша, которое ниже детализируем по всем направлениям
        if l.count(l[0]) == len(l) and l[0] != 0:
            return True
        else:
            return False
        
    # по горизонтали
    for row in game:
        if all_same(row):
            print(f"Игрок {row[0]} - победитель по горизонтали!")
            return True

    # по вертикали
    for col in range(len(game[0])):
        col_check = []
        for row in game:
            col_check.append(row[col])
        if all_same(col_check):
            print(f"Игрок {col_check[0]} - победитель по вертикали!")
            return True

    # по / диагонали
    diags = []
    for idx, reverse_idx in enumerate(reversed(range(len(game)))):
        diags.append(game[idx][reverse_idx])

    if all_same(diags):
        print(f"Игрок {diags[0]} - победитель по диагонали! (/)")
        return True

    # по \ диагонали
    diags = []
    for ix in range(len(game)):
        diags.append(game[ix][ix])
        
    if all_same(diags):
        print(f"Игрок {diags[0]} - победитель по диагонали! (\\)")
        return True

    # ничья
    tie_check = []
    for row in game:
        if(row.count(0) > 0):
            tie_check.append(row)
    if len(tie_check) == 0:
        print("Ничья!")
        return True

    return False # если ни одно из условий не выполнено, то продолжаем игру

def game_board(game_map, player=0, row=0, column=0, just_display=False):
    try:
        if game_map[row][column] != 0:
            print("Эта ячейка уже занята, попробуйте другую!")
            return False

        print ("  "+" ".join([str(i) for i in range(len(game_map))]))
        if not just_display:
            game_map[row][column] = player
        for count, row in enumerate(game_map):
            string_row = ' '.join([str(item) for item in row])
            formatted_row = string_row.replace("0", "-")
            formatted_row = formatted_row.replace("1", "x")
            formatted_row = formatted_row.replace("2", "o")
            print(count, formatted_row)
        return game_map
    except IndexError:
        print("Вы попытались ввести номер строки/колонки за пределами 0,1 или 2? (IndexError)")
        return False
    except Exception as e:
        print("Что-то пошло совсем не так.../n" + str(e))
        return False

play = True
players = [1, 2]
while play:
    game_size = 3
    game = []
    for i in range(game_size):
        row = []
        for i in range(game_size):
            row.append(0)
        game.append(row)

    game_won = False
    player_cycle = itertools.cycle([1, 2])
    game_board(game, just_display=True)
    while not game_won:
        current_player = next(player_cycle)
        played = False
        while not played:
            print(f"Игрок: {current_player}")
            try:
                column_choice = int(input("Номер колонки (0, 1 или 2)? "))
                row_choice = int(input("Номер строки (0, 1 или 2)? "))
                played = game_board(game, player=current_player,row=row_choice, column=column_choice)
            except ValueError:
                print("Нужно вводить цифры, а не буквы/символы! (ValueError)")

        if win(game):
            game_won = True
            again = input("Игра окончена, хотите сыграть снова? (y/n) ")
            if again.lower() == "y":
                print("Запускаем игру заново...")
            elif again.lower() == "n":
                print("До встречи!")
                play = False
            else:
                print("Некорректный ответ, но... до встречи!")
                play = False