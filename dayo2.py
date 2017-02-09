#Here we set up the keypad shit that Cloudy with a Chance of Meatballs did except not fake
KEYPAD = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
i, j = 1, 1
MAX_I = len(KEYPAD) - 1
MAX_J = len(KEYPAD[0]) - 1

print('PART 1')
# SNAKE TAKE THE ORDERS GODDAMNIT
with io.open('inputs/day2.txt','r') as f:
    line_nb = 0
    for instructions in f:
        for instruction in instructions:
        #same stuff as day one, except shorter?! wowzers what a day
            if instruction == 'U':
                i = max(0, i-1)
            elif instruction == 'L':
                j = max(0, j-1)
            elif instruction == 'D':
                i = min(MAX_I, i + 1)
            elif instruction == 'R':
                j = min(MAX_J, j + 1)
#you wanna know the passkey to Trump's mexican dungeon- I mean the shitter
        print('Code for line {}: {}'.format(line_nb, KEYPAD[i][j]))
        line_nb += 1


# parto dos

EMPTY_KEY = 0
KEYPAD = [[EMPTY_KEY, EMPTY_KEY, 1, EMPTY_KEY, EMPTY_KEY], 
          [EMPTY_KEY, 2, 3, 4, EMPTY_KEY], 
          [5, 6, 7, 8, 9],
          [EMPTY_KEY, 'A', 'B', 'C', EMPTY_KEY], 
          [EMPTY_KEY, EMPTY_KEY, 'D', EMPTY_KEY, EMPTY_KEY]]
i, j = 2, 0
MAX_I = len(KEYPAD) - 1
MAX_J = len(KEYPAD[0]) - 1

print('')
print('PART 2')
#gotta print that sorry ^ my dude
with io.open('inputs/day2.txt','r') as f:
#I need to get iT
    line_nb = 0
    for instructions in f:
        for instruction in instructions:
        #hOW COULD THIS HAPPEN TO MEEEEE- wow if the guy has time to figure this out maybe he doesn't need to shit that bad
            if instruction == 'U':
                new_i = max(0, i-1)
                if KEYPAD[new_i][j] != EMPTY_KEY:
                    i = new_i

            elif instruction == 'L':
                new_j = max(0, j-1)
                if KEYPAD[i][new_j] != EMPTY_KEY:
                    j = new_j

            elif instruction == 'D':
                new_i = min(MAX_I, i + 1)
                if KEYPAD[new_i][j] != EMPTY_KEY:
                    i = new_i

            elif instruction == 'R':
                new_j = min(MAX_J, j + 1)
                if KEYPAD[i][new_j] != EMPTY_KEY:
                    j = new_j
#fINALLY TIME TO RELIEVE MYSELF
        print('Code for line {}: {}'.format(line_nb, KEYPAD[i][j]))
        line_nb += 1
