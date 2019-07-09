""" A database file for words

  @author:  Arpit Malhotra  
    @contact: <arpitmalhotra12@gmail.com>

"""

import random


class StringDatabase():
    """Class for reading the file and storing words in a list. 
    
    Also stores the frequency for every letter and generates a random word for the game
    
    """
    finalwords = []
    frequency = {'a':8.17, 'b':1.49, 'c':2.78,
                 'd':4.25, 'e':12.70, 'f':2.23,
                  'g':2.02, 'h':6.09, 'i':6.97,
                   'j':0.15, 'k':0.77, 'l':4.03,
                    'm':2.41, 'n':6.75, 'o':7.51,
                     'p':1.93, 'q':0.10, 'r':5.99,
                      's':6.33, 't':9.06, 'u':2.76,
                       'v':0.98, 'w':2.36, 'x':0.15,
                        'y':1.97, 'z':0.07}

    def inputWordsInList(self):
        """ Reads a file four_letters.txt and stores them in a list
        
        Returns: A list of 4030 words
        
        """
        
        myfile = open("four_letters.txt", "r")
        filecontent = myfile.read()
        
        listofwords = filecontent.strip().split("\n")
        
        # print(listofwords)
        for word in listofwords:
            words = word.split(" ") 
            for w in words:
                self.finalwords.append(w)
                 
        # print(self.finalwords)
        return self.finalwords
    
    def getRandomWord(self):
        """ Really a simple method that generates random words
        
        Returns: A word
        """
        return random.choice(self.finalwords)
            
