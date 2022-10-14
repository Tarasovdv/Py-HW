# Создайте программу для игры в ""Крестики-нолики"".

def create_field():
    return ["_"]*9


def create_field_plan():
    return [str(x) for x in range(1, 10)]


def print_fiels(arr):
    for i in range(0, 9, 3):
        print(arr[i]+" " + arr[i+1] + " " + arr[i+2])


def check(arr, n):
    for i in range(0, 9, 3):
        if arr[i] == arr[i+1] == arr[i+2] == n:
            return "Win"
    for i in range(0, 3):
        if arr[i] == arr[i+3] == arr[i+6] == n:
            return "Win"
    if arr[0] == arr[4] == arr[8] == n or arr[2] == arr[4] == arr[6] == n:
        return "Win"
    return "False"


def append(a, s, arr):
    arr[a-1] = s


def start():
    print("Welcome to my game: Tic tac toe")
    print("This is fiels")
    print_fiels(create_field())
    print("\nThis is number of position. Remember this information. But if you   ")
    print_fiels(create_field_plan())


def check2(arr, n):
    if n > 0 and n < 10:
        if arr[n-1] == "_":
            return True


def game():
    start()
    arr = create_field()
    help = False
    player_1 = str.upper(input("Player number one: choose a symbol X or 0: "))

    while help == False:
        if player_1 == "X":
            player_2 = "0"
            help = True
        elif player_1 == "0":
            player_2 = "X"
            help = True
        else:
            player_1 = str.upper(input(
                "Player number one, you entered wrong symbol! choose a symbol X or 0 again: "))

    print("Player number two: your symbol: " + player_2 + '\n' + 'lets start!')
    count = 1
    while count < 10:
        if not count % 2 == 0:
            player_1_turn = int(
                input("\nPlayer one: Enter number of positoin: "))
            while not check2(arr, player_1_turn) == True:
                player_1_turn = int(input(
                    "\nPlayer number one, you entered wrong number: Enter number of positoin again: "))

            append(player_1_turn, player_1, arr)
            print_fiels(arr)
        else:
            player_2_turn = int(
                input("\nPlayer two: Enter number of positoin: "))
            while not check2(arr, player_2_turn) == True:
                player_2_turn = int(input(
                    "\nPlayer number two, you entered wrong number: Enter number of positoin again: "))
            append(player_2_turn, player_2, arr)
            print_fiels(arr)
        count += 1
        if check(arr, player_1) == "Win":
            print("Player number one: Congratulations!You win!!")
            break
        elif check(arr, player_2) == "Win":
            print("Player number two: Congratulations!You win!!")
            break
        else:
            if count == 9:
                print("No one win")


game()
