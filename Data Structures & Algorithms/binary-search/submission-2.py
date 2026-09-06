class Solution:
    def search(self, nums: List[int], target: int) -> int:
        counter = 0
        not_found = -1 
        for n in nums: 
            if n == target: 
                return counter
            else: 
                counter += 1 
        return not_found


