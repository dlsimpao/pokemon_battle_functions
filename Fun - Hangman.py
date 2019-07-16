#Hangman game
    
class word:
    def __init__(self, word, hint = "None"):
        self.word = word
        self.letterList = []
        [self.letterList.append(x) for x in word]

        self.guessedLetters = []
        
        self.length = len(self.word)
        self.blanks = ["___"]*self.length

        self.hint = hint
        
        self.penalty = 10


        
#starts the game and gives instructions
    def start(self):
        print("type \".guessLetter("")\" in front of your variable name to guess a letter.\n"\
              "type \".guessWord("")\" to guess the word.\n"\
              "type \".getHelp\" for help.")
        print("\n"*33)
        print(self.blanks)

    def getHelp(self):
        print("type \".guessLetter("")\" in front of your variable name to guess a letter.\n"\
              "type \".guessWord("")\" to guess the word.\n"\
              "type \".showCorrect\" to show correct guesses.\n"\
              "type \".showGuesses\" to show all guesses.\n"\
              "type \".getHint\" to show the user's given hint.")
    
    def getHint(self):
        return self.hint
    
    def getLength(self):
        return self.length

    def getLetters(self):
        return self.letterList

    def check(self):
        if self.blanks == self.letterList:
            print("You've guess all the letters! The word is '"+self.word+".'")
        if self.penalty == 0:
            print("The hangman has been hanged!")

    def showCorrect(self):
        return self.blanks

    def showGuesses(self):
        return self.guessedLetters


    #main - user guesses letter
    def guessLetter(self,letter):
        if letter.lower() not in [x.lower() for x in self.guessedLetters]:
            self.guessedLetters.append(letter)
            for i in range(self.length):
                if self.letterList[i].lower() == letter.lower():
                    self.blanks[i] = self.letterList[i]
            if isinstance(letter, str) and letter.lower() not in [x.lower() for x in self.letterList]: #-------------------isinstance()
                print("Keep trying!")
                self.penalty -= 1
                print("Time to Death:",self.penalty)
            else:
                print("You guessed right!")
        else:
            print("You've already guessed this letter!")
        self.check()
        return self.blanks

    def guessWord(self,word):
        if word.lower() != self.word.lower():
            print("Game over. The hangman has been hanged!")
            exit()
        else:
            print("Congratulations, you've won!")
            exit()
                
##main()
x = word("")
x.start()
#x.guessLetter("e")
