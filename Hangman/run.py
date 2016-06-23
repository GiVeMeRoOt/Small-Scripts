#!/usr/bin/env python
import ps3_hangman

def hangman(secretWord):
    #print "Loading word list from file..."
    #print "55900 words loaded."
    print "Welcome to the game, Hangman!"
    print "I am thinking of a word that is %d letters long."%len(secretWord)
    guesses = 8
    guessed = False
    availableLetters = "abcdefghijklmnopqrstuvwxyz"
    lettersGuessed = ['']
    while guesses>0 and (not guessed):
        print "-------------"
        print "You have %d guesses left."%guesses
        print "Available letters: %s"%availableLetters
        lguessed = str(raw_input("Please guess a letter: ")).lower()
        if lguessed in secretWord and lguessed in availableLetters:
            lettersGuessed.append(lguessed)
            availableLetters = availableLetters.replace(lguessed , "")
            a=""
            for i in secretWord:
                if i in lettersGuessed:
                    a +=i
                else :
                    a +=" _"
            print "Good guess: %s"%a
            if a == secretWord:
                guessed = True
            
            
        elif not lguessed in availableLetters:
            a=""
            for i in secretWord:
                if i in lettersGuessed:
                    a +=i
                else :
                    a +=" _"
            print "Oops! You've already guessed that letter:%s"%a
            if a == secretWord:
                guessed = True
            
        else :
            lettersGuessed.append(lguessed)
            availableLetters = availableLetters.replace(lguessed , "")
	    a=""
            for i in secretWord:
                if i in lettersGuessed:
                    a +=i
                else :
                    a +=" _"
            guesses -= 1
            print "Oops! That letter is not in my word:%s"%a
    
    print "-----------"
    if guessed :
        print "Congratulations, you won!"
    else :
        print "Sorry, you ran out of guesses. The word was %s"%secretWord


secretWord = ps3_hangman.chooseWord(ps3_hangman.loadWords()).lower()
hangman(secretWord)
