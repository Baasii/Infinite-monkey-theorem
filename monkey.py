from operator import truediv
import string
import random
import time

with open('hamlet.txt') as hamlet:
    with open('hamletLower.txt', "r+") as lower: #Open write mode 
        for word in hamlet:
            y = word.lower()
            lower.write(y) #Read hamlet and change it into lowercase

    with open('hamletLower.txt', "r") as lower: #Open in read mode
        with open('output.txt', 'r+') as output:
            #put = output.read()
            
            f = (lower.read().split()) #Read unique words and split
            

                       
            longest_word =  max(f, key=len) #Read longest word and its length
            shortest_word = min(f, key=len) #Read shortest word and its length

            longestLength = len(longest_word)
            shortestLength = len(shortest_word)
            
            
            with open('foundWords.txt', 'a+') as correctWords:
                print('Starting comparison')
                letters = string.ascii_lowercase + string.punctuation
                loop = True
                foundCount = 0
                currentWord=0
                while(loop):
                    inputLength = random.randint(shortestLength, longestLength) #Generate random length between shortest and longest word
                    typedWord = ( ''.join(random.choice(letters) for i in range(inputLength)) ) #Random string
                    print(typedWord)
                    time.sleep(0.00011) #Time between comparisons
                    typedWord = "francisco"

                    
                    if typedWord == f[currentWord]: #If string is found in Hamlet ->      
                        currentWord +=1
                        correctWords.write(typedWord + ' ') #Write found word into correctWords
                        print('FOUND !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
                        print('Word found: ' + typedWord)
                        foundCount+=1 #How many words found
                        print(foundCount, ' words found')
                        

                        time.sleep(2.2)
                    

                    ###### TODO ######
                    # Fix write found words
                    # Subprocess
                    





