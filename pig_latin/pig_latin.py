
def toPigLatin(word):
    #if this is an empty word, don't do anything
    if len(word) < 1:
        return
    
    first_letter = word[0] #find the first letter of given word
    if first_letter in "aeiou": #the first letter is a vowel
        word_to_return = word + "ay" #we could also write: word += "-ay"
    else: #the first letter is a constanant
        """TODO:
            1. Set word_to_return equal to given word, but with the first letter
                sliced off. Use a colon (slice operator) to do this.
                    ex: my_word = "unhappy"
                        new_word = my_word[2:7]
                        print new_word     <-- prints out "happy"
            2. Add the first_letter of given word to the end of word_to_return
            3. Add the suffix "ay" to the end of word_to_return
        """
    return word_to_return

#Once you have finished, run this in your shell by hitting F5 or
#by clicking "Run" in the toolbar, and selecting "Run Module"

#You should be able to do stuff like:
    #print toPigLatin("pardon")   --> prints out "ardonpay"

#If you have more time, try adding new rules using more else if statements.
    #This function isn't perfect.
    #For example, with this function, toPigLatin("school") --> returns "choolsay"
        #when perhaps we'd want it to return "oolschay"
