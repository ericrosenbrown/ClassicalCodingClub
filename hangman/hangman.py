import linecache
import random

noose0 = '      _______'
noose1 = '     |/      |'
noose2 = '     |      '
noose3 = '     |      '
noose4 = '     |       '
noose5 = '     |      '
noose6 = '     |'
noose7 = '    _|___'

man0 = '(_)'
man1 = '\|/'
man2 = '|'
man3 = '/ \\'

noose_ascii = [noose0, noose1, noose2, noose3, noose4, noose5, noose6, noose7]
man_ascii = [man0, man1, man2, man3]

def print_hangman(bodyparts):
    to_print = [noose0, noose1]
    if bodyparts > 0:
        to_print.append(noose2 + man0)
    else:
        to_print.append(noose2)
    if bodyparts == 2:
        to_print.append(noose3 + ' |')
    elif bodyparts == 3:
        to_print.append(noose3 + '\|')
    elif bodyparts > 3:
        to_print.append(noose3 + man1)
    else:
        to_print.append(noose3)
    if bodyparts > 4:
        to_print.append(noose4 + man2)
    else:
        to_print.append(noose4)
    if bodyparts == 6:
        to_print.append(noose5 + '/')
    elif bodyparts > 6:
        to_print.append(noose5 + man3)
    else:
        to_print.append(noose5)
    to_print.append(noose6)
    to_print.append(noose7)
    for i in range(len(to_print)):
        print to_print[i]
    print ''
def play():           
    my_word = linecache.getline('dictionary.txt', random.randrange(1, 178686)).strip()
    correct_not_guessed = my_word #letters in my_word that haven't been guessed yet
    letters_guessed = []
    for j in range(len(my_word)):
        letters_guessed.append('_')

    print 'My word is ' + str(len(my_word)) + ' letters long\n'
    strikes = 0
    while True:
        print "correct guesses: " + str(letters_guessed[:len(my_word)])
        print "incorrect guesses: " + str(letters_guessed[len(my_word):])
        print_hangman(strikes)
        letter = raw_input("take a guess: ").lower()
        if letter == "quit":
            break
        if len(letter) > 1:
            print ">>>please enter only one letter per guess"
            print "--------------------------------------------------------------------------"
            continue
        if letter in letters_guessed:
            print ">>>you've already guessed the letter \"" + letter + '\". try again!'
            print "--------------------------------------------------------------------------"
            continue
        if not letter in correct_not_guessed:
            letters_guessed += letter
            strikes += 1
            if strikes > 6:
                print '>>>you lose :('
                print '>>>my word was: ' + my_word
                print_hangman(strikes)
                break
            print ">>>nope! try again"
        else:
            for k in range(len(my_word)):
                if my_word[k] == letter:
                    letters_guessed[k] = letter
            correct_not_guessed.translate(None, letter) #remove letter from correct_not_guessed
            print '>>>you guessed a letter in my word!'
        if not '_' in letters_guessed:
            print '>>>you win! you guessed my word: ' + my_word
            break
        print "--------------------------------------------------------------------------"
    play_again = raw_input("play again? (y/n)").lower()
    print
    if 'y' in play_again:
        return True
    else:
        return False

keep_playing = True
while keep_playing:
    keep_playing = play()
