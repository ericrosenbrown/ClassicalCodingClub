a)
print ">>>you've already guessed the letter \"" + letter + '\". try again!'
print "--------------------------------------------------------------------------"
continue
b)
return False
c)
for k in range(len(my_word)):
    if my_word[k] == letter:
        letters_guessed[k] = letter
correct_not_guessed.translate(None, letter) #remove letter from correct_not_guessed
print '>>>you guessed a letter in my word!'
d)
break
e)
letters_guessed += letter
strikes += 1
if strikes > 6:
    print '>>>you lose :('
    print '>>>my word was: ' + my_word
    print_hangman(strikes)
    break
    print ">>>nope! try again"
f)
print '>>>you win! you guessed my word: ' + my_word
break
h)
return True
g)
print ">>>please enter only one letter per guess"
print "--------------------------------------------------------------------------"
continue
