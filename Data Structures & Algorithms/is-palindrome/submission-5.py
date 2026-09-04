class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = '' #Is a string with no special characters 
        for c in s: 
            if c.isalnum(): 
                newStr += c.lower()
        return newStr == newStr[::-1]



 

    


        