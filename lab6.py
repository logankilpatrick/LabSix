#Lab 6
#Logan Kilpatrick
#November 1st, 2017


#fileNames = ["english.txt", "french.txt", "german.txt", "italian.txt", "spanish.txt"]
#declared global so it can be a constant. Also makes it easier to switch files if we needed to.   

def printVowels(holderList):
    '''
    takes in a list containing a dictonary, name of the file, and ratio of vowels to total letters.
    does not return any values.
    simply prints the desired info.
    
    '''
    letterCount = holderList[0]
    printedName = holderList[1]
    ratio = holderList[2]
    
    print(printedName)
    for word in sorted(letterCount):
        print(word+ ":", letterCount[word])
    print("Total vowels / total letters: ", "%.2f"  %(ratio * 100), "%")
    print()

def analysisTool(fileName, printedName):
    '''
    accpets in the name of the file we want to work with.
    returns a list containing the dictonary of letters, name of the file, and th ratio.
    only does analysis of data! 
    '''
    letterCount = {}
    totalLetterCounter = 0
    vowelCounter = 0
    with open(fileName, encoding = "latin-1") as infile:
        for line in infile:
            #line = line.rstrip('.!,') #strips away punctuation 
            wordList = line.split()
            for word in wordList:
                for letter in word:
                    totalLetterCounter += 1
                    letter = letter.upper()#this part is key. Makes igt case insensative                                          
                    if letter == "A" or letter == "E" or letter == "I" or letter == "O" or letter == "U":
                        letterCount[letter] = letterCount.get(letter, 0) + 1
                        vowelCounter += 1
                    
                    
                        
    ratio = (vowelCounter / totalLetterCounter)  
    holderList = [letterCount, printedName, ratio]
    return (holderList)
   

def main():
    '''
    takes n no parameters
    returns nothing
    loops through a list of file names. uses excpetion handeling to make sure its a real file. 
    calls the analysis function, and then the print function for each element of the fileNames list.  
    '''
    fileNames = ["english.txt", "french.txt", "german.txt", "italian.txt", "spanish.txt"]
    #file names could be made global! 
    printedName = ""
    #start of loop
    holderList = []
    for r in range(len(fileNames)):
        try:
            with open(fileNames[r], encoding = "latin-1") as infile:#this hsould probaly happen in the analysis function! 
                if fileNames[r] == "english.txt":
                    printedName = "English"
                elif fileNames[r] == "french.txt":
                    printedName = "French" 
                elif fileNames[r] == "german.txt":
                    printedName = "German"
                elif fileNames[r] == "italian.txt":
                    printedName = "Italian"  
                elif fileNames[r] == "spanish.txt":
                    printedName = "Spanish"  
                holderList = analysisTool(fileNames[r], printedName)#pass the file name! 
                printVowels(holderList)
        except FileNotFoundError as e:
            print(e)  
main()