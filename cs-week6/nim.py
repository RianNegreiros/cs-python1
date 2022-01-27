def machine_choose_play(n, m):
    machine_remove = 1

    while machine_remove != m:
        if (n - machine_remove) % (m + 1) == 0:
            return machine_remove

        else:
            machine_remove += 1

    return machine_remove


def user_choose_play(n, m):
    valid_play = False

    while not valid_play:
        player_remove = int(input('How many pieces will you remove ? '))

        if player_remove > m or player_remove < 1:
            print('\nOops! Invalid play! Try again.', end='\n')
        else:
            valid_play = True

    return valid_play


def championship():
    n_round = 1
    while n_round <= 3:
        print()
        print('\n**** Round', n_round, '****', end='\n')
        match()
        n_round += 1
    print()
    print('Score: You 0 X 3 Machine')


def match():
    n = int(input('How many pieces ? '))

    m = int(input('Limit of pieces per turn ? '))

    machine_turn = False

    if n % (m + 1) == 0:
        print('\nYou start!')

    else:
        print('\nThe machine start!')
        machine_turn = True

    while n > 0:
        if machine_turn:
            machine_remove = machine_choose_play(n, m)
            n = n - machine_remove
            if machine_remove == 1:
                print('\nThe machine removed')
            else:
                print('\nThe machine removed', machine_remove, 'pieces')

            machine_turn = False
        else:
            user_remove = user_choose_play(n, m)
            n = n - user_remove
            if user_remove == 1:
                print()
                print('You removed one piece')
            else:
                print()
                print('You removed', user_remove, 'pieces')
            machine_turn = True
        if n == 1:
            print('Now remain one piece on the board', end="\n")
            print()
        else:
            if n != 0:
                print('Now remain,', n, 'pieces on the board.', end="\n")

    print('Game Over! The machine won')


print('Welcome to NIM game. Choose:')
print()

print('1 - to play an isolated game')

match_type = int(input('2 - to play championship '))

if match_type == 2:
    print()
    print('You choose championship!')
    print()
    championship()
else:
    if match_type == 1:
        print()
        match()
