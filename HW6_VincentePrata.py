"""

Vincente Prata
CS 100 2020F Section 019
HW 06, September 25, 2020
"""

# Define "has final letter" function

def hasFinalLetter(strList,letters):
    result = []
    for word in strList:
        lastLetter = word[-1]
        for letter in letters:
            if letter == lastLetter:
                result.append(word)
    return(result)

# Test Case One

strList = ['Banana', 'Pineapple', 'Pizza']
letters = "cghijCGHIJ"
print(hasFinalLetter(strList,letters))

#Test Case Two

strList = ['Famous', 'Celebrity', 'Star']
letters = "srtvuSRTVU"
print(hasFinalLetter(strList,letters))

#Test Case Three

strList = ['Mexico', 'Italy', 'Portugal']
letters = "oylgtOYLGT"
print(hasFinalLetter(strList,letters))


#Define "is divisible" function


def isDivisible(maxInt,twoInts):
    result = []
    for num in range(1,maxInt):
        intOne = twoInts[0]
        intTwo = twoInts[1]
        divisibility = num % intOne + num % intTwo
        if divisibility == 0:
            result.append(num)
    return(result)


#Test Case One

maxInt = 5
twoInts = (2,5)
print(isDivisible(maxInt,twoInts))

#Test Case Two

maxInt = 21
twoInts = (2,5)
print(isDivisible(maxInt,twoInts))

#Test Case Three

maxInt = 8
twoInts = (1,7)
print(isDivisible(maxInt,twoInts))


        
   
       
    
    
        
             
    







        







        
        


        






        
