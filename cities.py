cities = set([])


def player_turn():
    city = input('Ваш ход!\nВедите город:')
    if city in cities:
        print('Такой город уже был, пожалуйста, введите другой!')
        player_turn()
    else:
        cities.add(city.upper())


def turner():
    return True


def bot_turn(valid='true'):
    if valid == 'true':
        with open('cities.txt', 'r', encoding='utf-8') as file:
            for line in file:
                s = list(cities)[-1][-1]
                if line[0] == s:
                    cities.add(line)
                    print(f'Вам на {line[0]} ')


def main():
    if input('Хотите ходить первым? y/n') == 'y' or input('Хотите ходить первым? y/n') == 'Y':
        while True:
            player_turn()
            bot_turn()
            print(cities)
    else:
        while True:
            bot_turn('false')
            player_turn()


main()
