# take an input string of a single word, return a string wherein every letter of the input string is either 'x' if that letter only appeared once, or 'y' if it appeared more than once.

Word = str(input('Input a word'))

def ChangeWord(word):

    Dictionary = dict((letter,word.count(letter)) for letter in set(word))
    #characters = list(word)
    newword = str()
    for letter in word:
        if Dictionary[letter] == 1:
            newword += 'x'
        else:
            newword += 'y'
    return newword

print(ChangeWord(Word))
