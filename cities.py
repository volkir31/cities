cities = []


def player_turn():
    city = input('Ваш ход!\nВедите город:')
    if city.upper() in cities:
        print('Такой город уже был, пожалуйста, введите другой!')
        player_turn()
    else:
        city = city.replace(' ', '')
        with open('cities.txt', 'r', encoding='utf-8') as file:
            for line in file:
                if line.upper() != city.upper():
                    print('Такого города нет, пожалуйста, введите другой город')
                    player_turn()
                else:
                    continue
        if len(cities) == 0:
            cities.append(city.upper())
            print(city.title())
        else:
            if cities[-1][-1] == 'Ь' or cities[-1][-1] == 'Ы' or cities[-1][-1] == 'Ё' or cities[-1][-1] == 'Ъ':
                if city[0].upper() != cities[-1][-2]:
                    print(f'Вы ввели город, начинающийся на букву {city[0]}, а нужно - на букву {cities[-1][-2]}')
                    player_turn()
            else:
                if city[0].upper() != cities[-1][-1]:
                    print(f'Вы ввели город, начинающийся на букву {city[0]}, а нужно - на букву {cities[-1][-1]}')
                    player_turn()


def bot_turn(valid='true'):
    if valid == 'true':
        with open('cities.txt', 'r', encoding='utf-8') as file:
            for line in file:
                if cities[-1][-1] == 'Ь' or cities[-1][-1] == 'Ы' or cities[-1][-1] == 'Ё' or cities[-1][-1] == 'Ъ':
                    s = cities[-1][-2]
                else:
                    s = cities[-1][-1]
                    line = line.replace("\n", "")
                    if line.upper() in cities:
                        continue
                    else:
                        if line[0] == str(s).upper():
                            cities.append(line.upper())
                            if line[-1] =='ь' or line[-1] =='ы' or line[-1] == 'ё' or line[-1] =='ъ':
                                print(f'{line.title()}\nВам на {line[-2].upper()} ')
                            else:
                                print(f'{line.title()}\nВам на {line[-1].upper()} ')
                            break


def main():
    if input('Хотите ходить первым? y/n\n') == 'y' or input('Хотите ходить первым? y/n\n') == 'Y':
        while True:
            player_turn()
            bot_turn()
    else:
        while True:
            bot_turn()
            player_turn()


main()
