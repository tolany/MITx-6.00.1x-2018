# Problem 1 - Is the Word Guessed
# 10.0/10.0 points (graded)
# Please read the Hangman Introduction before starting this problem. We'll start by writing 3 simple functions that will help us easily code the Hangman problem. First, implement the function isWordGuessed that takes in two parameters - a string, secretWord, and a list of letters, lettersGuessed. This function returns a boolean - True if secretWord has been guessed (ie, all the letters of secretWord are in lettersGuessed) and False otherwise.

# Example Usage:

# >>> secretWord = 'apple'
# >>> lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
# >>> print(isWordGuessed(secretWord, lettersGuessed))
# False
# For this function, you may assume that all the letters in secretWord and lettersGuessed are lowercase.

#--------------------- code ------------------------#


def isWordGuessed(secretWord
, lettersGuessed):
    '''
    
    secretWord: string, the
    word the user is guessing
    lettersGuessed: list, wh
    at letters have been guessed so far
    returns: boolean, True i
    f all the letters of secretWord are in lettersGuessed;
    
      False otherwise
      
    '''
    
    for letter in list(secre
    tWord):
        if len(secretWord) =
        = 1:
            if letter in let
            tersGuessed:
                return True
                
        else:
            
            if letter in let
            tersGuessed:
                return isWor
                dGuessed(secretWord[1::], lettersGuessed)
            else:
                
                return False
                
# --------------------- result ---------------------#
# Correct
