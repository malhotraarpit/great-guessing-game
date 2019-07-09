""" A file for specific storing game data

  @author:  Arpit Malhotra  
    @contact: <arpitmalhotra12@gmail.com>

"""


class Game():
    """ A class for storing the game data such as score, word, status etc"""
    
    score = 0 
    word = ""
    status = ""
    noOfGuess = 0
    missedletters = 0
    finalscore = 0
    countOfLetters = 0
    
    def __init__(self, word):
        """A constructor for initializing word when a new object of game is created
        
        Parameters:
            word: A word assigned for this game
        """
        
        self.word = word
    
