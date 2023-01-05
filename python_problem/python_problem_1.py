num = 0


def brGame(input_num):
    while True:
        try:
            if 1 <= input_num <= 3:
                break
            else:
                print('1,2,3 중 하나를 입력하세요.')
        except ValueError:
            print('정수를 입력하세요.')


while num < 31:

    input_num = int(input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) : "))
    brGame(input_num)

    for _ in range(input_num):
        num += 1
        print(f'playerA : {num}')
        if num == 31:
            print('playerB win!')
            break

    if num >= 31:
        break

    input_num = int(input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) : "))
    brGame(input_num)

    for _ in range(input_num):
        num += 1
        print(f'playerB : {num}')
        if num == 31:
            print('playerA win!')
            break
