#First passing attempt

import numpy as np
class Solution(object):
    def getFinalState(self, nums, k, multiplier):
        """
        :type nums: List[int]
        :type k: int
        :type multiplier: int
        :rtype: List[int]
        """
        
        for x in range(k):
            x+=1
            min_index = np.argmin(nums)
            nums[min_index]*=multiplier

        return nums


#optimizing attmept


class Solution(object):
    def getFinalState(self, nums, k, multiplier):
        for i in range(k):
            curr_min = min(nums)
            min_index= nums.index(curr_min)
            nums[min_index]*=multiplier
        return nums
