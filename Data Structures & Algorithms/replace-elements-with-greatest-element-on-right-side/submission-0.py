class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        #Initial max can be set to -1 
        #Reverse iteration 
        #new max = max(oldMax, arr[i])
        rightMax = -1
        for i in range(len(arr) - 1, -1, -1): #This is how you iterate in reverse on an array 
                newMax = max(rightMax, arr[i])
                arr[i] = rightMax 
                rightMax = newMax
        return arr







        
        