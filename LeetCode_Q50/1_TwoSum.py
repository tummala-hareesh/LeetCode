class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """Return indices of the two numbers such that they add up to target.
        
        Parameters
        ----------
        nums : int
            List of numbers
        target : str
            add up to this target

        Returns
        -------
        List[int] : int
            List of 2 integers that sum up to target
        """        
        
        n = len(nums)
        
        if n == 2:
            return [0, 1]
        else:
            for i in range(n):
                rem = target - nums[i]
                if rem in nums:
                    index = nums.index(rem)
                    if index != i:
                        return [i, index]          
