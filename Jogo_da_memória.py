# Welcome screen
print("""
 ╔══════════════════════════════════╗
 ║                                  ║
 ║           Memory Game            ║
 ║                                  ║
 ╚══════════════════════════════════╝
""")

# Import random library for the rest of the code
import random

square = 0
# A loop to define the board size
while square == 0:
    try:
        num = int(input('Enter the the number of columns and lines your square matrix will have (even number): '))
        if num > 1 and num <=10 and num%2 == 0:
            square = num
            break
        else: 
            print('Number must be a even numb. Min is 2, max is 10')
            continue # Goes to the next iteration
    except ValueError: # Error treatment
        print('Number must be an integer')
        continue
print(f'Okay! Your matrix will have {square} columns and lines')

matrix = [] # Creating the matrix of the position of the elements and where the True or False check will be made
for i in range(square):
    row = []
    for j in range(square):
        row.append(0)
    matrix.append(row)

for i in range(square): # Saving the element positions
    for j in range(square):
        matrix[i][j] = int(f'{i+1}{j+1}')

# Randomizing the elements that will appear on the board
elements = ['AA', 'AA', 'BB', 'BB', 'CC', 'CC', 'DD', 'DD', 'EE', 'EE', 'FF', 'FF', 'GG', 'GG', 'HH', 'HH', 'II', 'II', 'JJ', 'JJ', 'KK', 'KK', 'LL', 'LL', 'MM', 'MM', 'NN', 'NN', 'OO', 'OO', 'PP', 'PP', 'QQ', 'QQ', 'RR',  'RR', 'SS', 'SS', 'TT', 'TT', 'UU', 'UU', 'VV', 'VV', 'WW', 'WW', 'XX', 'XX', 'YY', 'YY', 'ZZ', 'ZZ','※※', '※※', 'αα', 'αα', '₠₠', '₠₠', 'ÆÆ', 'ÆÆ', 'ĦĦ', 'ĦĦ', '⩎⩎', '⩎⩎',  'aa', 'aa','bb','bb','cc','cc','dd','dd','ee','ee','ff','ff','gg', 'gg','hh','hh','ii','ii','jj','jj','kk','kk','ll','ll','mm','mm','nn','nn','oo','oo','pp','pp','qq','qq','rr','rr','ss','ss','tt','tt','uu','uu','vv','vv','ww','ww','xx','xx','yy','yy','zz','zz']
size = square**2
m_elements = elements[0:size]
random.shuffle(m_elements) # Doing a shuffle to make sure that the elements are randomly arranged in the matrix

elements_matrix =  [] 
for i in range(square):
    row = []
    for j in range(square):
        row.append(m_elements[i*square+j])
    elements_matrix.append(row)

# At the beginning of the game, no elements were discovered
for i in range(square):
    for j in range(square):
        matrix[i][j] = False

# A function to check if the game is over or should continue
def check_false(lang):
    for i in range(len(lang)):
        for j in range(len(lang)):
            if lang[i][j] == False:
                return True
    return False

# An extra function to print the game board on the first move only
def first_display():
    board = ""
    for i in range(square):
        for j in range(square):
            board += f'({i+1},{j+1})'
            board += ' '
        board += '\n'
    print(board)

# A function to show the matrix after the user give invalid inputs for the positions
def display_playboard_middle_play(a,b):
    board = ""
    for i in range(square):
        for j in range(square):
            if matrix[i][j] is True or (matrix[i][j] is False and (i == a and j == b)):
                board += f'{elements_matrix[i][j]}'
            else:
                board += f'({i+1},{j+1})'
            board += ' '
        board += '\n'
    print(board)

# A function to print out the matrix after the user's wrong choices for a match
def display_playboard_after_chooses(a,b,c,d):
    board = ""
    for i in range(square):
        for j in range(square):
            if matrix[i][j] is True or (matrix[i][j] is False and ((i == a and j == b) or (i ==c and j == d))):
                board += f'{elements_matrix[i][j]}'
            else:
                board += f'({i+1},{j+1})'
            board += ' '
        board += '\n'
    print(board)

# A function to show the matrix after the user choices
def display_playboard_while_or_after_play():
    board = ""
    for i in range(square):
        for j in range(square):
            if matrix[i][j] is True:
                board += f'{elements_matrix[i][j]}'
            else:
                board += f'({i+1},{j+1})'
            board += ' '
        board += '\n'
    print(board)

# A function that will result in the player's moves and continue until the game is over
def playing():
    a = None
    b = None
    c = None
    d = None
    while a is None or b is None or c is None or d is None:
        try:
            while a is None:
                a = int(input(f'Row: '))-1
                if a == -1:
                    print("\nError: selected row can't be zero")
                    a = None
                    display_playboard_middle_play(a,b)
                    continue  # Continue to the next iteration if a is invalid
                elif a > square-1:
                    print(f"\nError: selected row exceeds board's size! Select row again")
                    a = None
                    display_playboard_middle_play(a,b)
                    continue  # Continue to the next iteration if a is invalid
            while b is None:
                b = int(input(f'Column: '))-1
                if b == -1:
                    print("\nError: selected column can't be zero")
                    b = None
                    display_playboard_middle_play(a,b)
                    continue  # Continue to the next iteration if b is invalid
                elif b > square-1:
                    print(f"\nError: selected column exceeds board's size! Select column again")
                    b = None
                    display_playboard_middle_play(a,b)
                    continue  # Continue to the next iteration if b is invalid
            if matrix[a][b] is True:
                print('\nThis position has already been discovered, select again')
                a = None
                b = None
                display_playboard_middle_play(a,b)
                break
            if a != None and b != None:
                display_playboard_middle_play(a,b)
            while c is None:
                c = int(input(f'Row: '))-1
                if c == -1:
                    print("\nError: selected row can't be zero")
                    c = None
                    display_playboard_middle_play(c,d)
                    continue  # Continue to the next iteration if c is invalid
                elif c > square-1:
                    print(f"\nError: selected row exceeds board's size! Select row again")
                    c = None
                    display_playboard_middle_play(c,d)
                    continue  # Continue to the next iteration if c is invalid
            while d is None:
                d = int(input(f'Column: '))-1
                if d == -1:
                    print("\nError: selected column can't be zero")
                    d = None
                    display_playboard_middle_play(c,d)
                    continue  # Continue to the next iteration if d is invalid
                elif d > square-1:
                    print(f"\nError: selected column exceeds board's size! Select column again")
                    d = None
                    display_playboard_middle_play(c,d)
                    continue  # Continue to the next iteration if d is invalid
                elif a == c and b == d:
                    print("\nYou've selected the same element twice! Select the second once again")
                    c = None
                    d = None
                    break  # Continue to the next iteration if c or d is invalid
                if matrix[c][d] is True:
                    print('\nThis position has already been discovered, select the second once again')
                    display_playboard_middle_play(a,b)
                    c = None
                    d = None
                    break  # Continue to the next iteration if c or d is invalid
                if elements_matrix[a][b] == elements_matrix[c][d]:
                    matrix[a][b] = True
                    matrix[c][d] = True
                    print(f'\nCongratulations, you got it!')
                else:
                    print('\nThese are the cards you selected:')
                    display_playboard_after_chooses(a,b,c,d)
                    print(f'\nNo match, unfortunately...')
        except ValueError:
            print(f'\nError: your number needs to be an integer and be between 1 to {square}! Try again')
            display_playboard_while_or_after_play()
            continue
        if a != None and b != None and c != None and d !=None:
            display_playboard_while_or_after_play()

# Part of the code that prints the board for the first time and a loop 
# and a condition that checks when the game continues and when it ends        
first_display()
while check_false(matrix) == True:
    playing()
if check_false(matrix) == False:
    print("            .     *          ")
    print("   *                           ")
    print("              .         .     ")
    print("             *                ")
    print("          .            *      ")
    print("   .            .        .    ")
    print("       *              .       ")
    print("                               ")
    print("   Congrats, you've done it!    ")
    print("       .   *        .         ")
    print("     *       .           *    ")
    print("                .       .     ")
    print("            .     *          ")
    print("   *                           ")
    print("              .         .     ")
    print("             *                ")
    print("          .            *      ")

