PIN = 5555
count = 3

while True:
    userpin = int(input("Введите ПИН: "))

    if userpin == PIN:
        print("Пин верен!")
        break
    elif userpin != PIN and count > 1:
        count -= 1
        print(f"Пин не верен. У Вас осталось {count} попыток")
    else:
        print("Обратитесь в банк")
        break
