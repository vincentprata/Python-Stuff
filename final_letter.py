# Created by Vincente Prata

"""
The function "hasFinalLetter" takes two parameters: strList (a list of non-empty strings)
and letters (a string of upper and/or lower case letters). This function creates and returns
a list of all the strings in strList that end with a letter in letters. Three test cases were
created, each consisting of a list of non-empty strings and a string of upper and/or lower
case letters. The first test case returns the empty list because it none of the strings in strList
end with a letter in letters.
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




        
   
       
    
    
        
             
    







        







        
        


        






        
