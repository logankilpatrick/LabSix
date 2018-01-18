# Module 6 exercises

# 1. Textbook R8.8
# In programs, the months are often numeric values 1-12.
# Suppose you need to write a program that needs to print the
# month names from the month number, which would you use?
# A list, set, or dictionary?
#dictonayr key: 1-12, value: month
#same thing for list and tuple


# If you need to write a program that needs to print the
# month numbers from the month names, which would you use?



# 2. Write a function that takes 2 string arguments and returns
# a. a set of letters that are contained in both strings
# b. a set of letters that are not contained in either strings
# c. a set of non-letters that are in both strings


#In comprehension we assume that we are adding to an iterbale.  That is why we dont need to put letters1.add(c)! It is assumed! 
'''
def lettersInBoth(s1, s2):

    letters1 = { c for c in s1 if c.isalpha() }#set comprehension 
    letters2 = { c for c in s2 if c.isalpha() }
    
    return (letters1.intersection(letters2))
            
def notInEither(s1, s2):
    allLetters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    letters1 = { c for c in s1 if c.isalpha() }#set comprehension 
    letters2 = { c for c in s2 if c.isalpha() }
    totalLetters = letters1.union(letters2)
    return (allLetters.difference(totalLetters))

def nonLettersBoth(s1, s2):
    nonletters1 = { c for c in s1 if c.isalpha() }#set comprehension 
    nonletters2 = { c for c in s2 if c.isalpha() }

    return (nonletters1.union(nonletters2))


str1 = "Guido Van Rossum first came up with Python in the late 1980s."
str2 = "Rossum released the first version of Python code (0.9.0) in February 1991."
both = lettersInBoth(str1, str2)
#neither = notInEither(str1, str2)
#commonNonLetters = nonLettersBoth(str1, str2)

print("Letters in both:", both)
#print("Letters in neither:", neither)
#print("Non letters in both:", commonNonLetters)


'''
# 3. Textbook P8.5
# Write a program that counts how often each word occurs 
# in a file.
'''
try:
    with open("mod6exInput.txt") as infile:
        wordCount = {}
        for line in infile:
            line = line.rstrip('.!,') #strips away punctuation 
            wordList = line.split()
            for word in wordList:
              #appends it to a dictonary
               
                #slower way to do so 
                #if word not in wordCount:
                #    wordCount[word] = 1    #if word does not exist, it will add word and 1 to the dictonary
                #else:
                #    wordCount[word] += 1   #if word exists, it will modify vlaue of key word 
               
               
                wordCount[word] = wordCount.get(word, 0) + 1
                #goes to key word.  either get the actual value or zero. either way, we add one to it.
                #if word does not yet exist, returns 0 plus 1.
                #if word exist, get returns the value plus one.  (increments it) 
                #dictonaries are the tool to keep track of multiple items.... keep count of things... frequency count problem 
                
    for word in sorted(wordCount):
        print(word, wordCount[word])
        
except FileNotFoundError as e:
    print(e)

'''
'''
# 4. How do you tell if there are duplicates in a list?
mylist = [2,3,9,11,2,4,7]
if len(myList) > len(set(mylist)):
    print("Duplicate")
else:
    print("no duplicate")

next best solution, use a dictonary
most painful solution, loop through manually.  


'''
# 5. How do you construct a dictionary from a list of tuples?
summer = [("june",6), ("july",7), ("august",8)]

summerDictionary = dict(summer)

print(summerDictionary)
# 6. How do you construct a dictioinary from 2 parallel lists?
name = "January February March".split()      # what does this do? Makes a list of strings 
num = [1,2,3]

winterDictionary = dict(zip(name, num))
print(winterDictionary)

#is they arent parrel(linned up in length), it will ignore the non symetrical lengths and ignore them 

