# Problem 5 - Playing a Hand
# 10.0/10.0 points (graded)
# In ps4a.py, note that in the function playHand, there is a bunch of pseudocode. This pseudocode is provided to help guide you in writing your function. Check out the Why Pseudocode? resource to learn more about the What and Why of Pseudocode before you start coding your solution.

# Note: Do not assume that there will always be 7 letters in a hand! The parameter n represents the size of the hand.

# Testing: Before testing your code in the answer box, try out your implementation as if you were playing the game. Here is some example output of playHand:

# --------------------------- code --------------------------- #
def playHand(hand, wordList, n):
    totalScore = 0
    while calculateHandlen(hand) > 0:
        c_hand = displayHand(hand)
        print("Current hand " + str(c_hand),end=" ")
        word = input(str('Enter word, or a "." to indicate that you are finished: '))
        if word == ".":
            print("Goodbye! Total score: " + str(totalScore) + " points.")
            break
        else:
            if isValidWord(word,hand, wordList) != True:
                print("Invalid word, please try again.")
                print("")
            else:
                wordScore = getWordScore(word, n)
                totalScore += wordScore
                print('" ' + word + ' "' + " earned " + str(wordScore) + " points. Total: " + str(totalScore) + " points")
                print("")
                hand = updateHand(hand, word)
    else:
        print("Run out of letters. Total score: " + str(totalScore) + " points.")
        
        
# ----------------------------result ------------------------#
# CORRECT