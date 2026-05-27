class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Create a hash set
        seen = set()

        # Iterate through the array
        for num in nums:
            # Check if the number is in the array (O(1))
            if num in seen:
                return True
            
            # If the number isn't in the hash, add it. 
            seen.add(num)
        return False