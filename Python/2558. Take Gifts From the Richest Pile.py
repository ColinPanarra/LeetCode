import numpy as np
class Solution(object):
    def pickGifts(self, gifts, k):
        """
        :type gifts: List[int]
        :type k: int
        :rtype: int
        """


        taken_gifts = 0
        seconds = 0 
        total_gifts = floor(np.sum(gifts))
        gifts = np.array(gifts)

        while seconds < k:
            curr_max = max(gifts)
            index = gifts.argmax()
            leave = floor(math.sqrt(curr_max))
            gifts[index] = leave
            taken_gifts+= curr_max - leave
            seconds+=1
        
        gifts_left = total_gifts - taken_gifts
        return int(gifts_left)
