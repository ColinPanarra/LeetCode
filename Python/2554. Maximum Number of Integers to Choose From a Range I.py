class Solution(object):
    def maxCount(self, banned, n, maxSum):
        """
        :type banned: List[int]
        :type n: int
        :type maxSum: int
        :rtype: int
        """

        sum=0 
        count=0
        x=1
        pointer=0 
        banned = list(set(banned))
        banned.sort()
        
        
        while x<=n:
            if  pointer<len(banned) and x==banned[pointer]:
                x+=1
                pointer+=1
                continue
            else: 
                testSum = sum + x
                if testSum>maxSum:
                    return count
                if testSum==maxSum:
                    return count+1
                sum+=x
                count+=1
            x+=1 
            

        if sum <= maxSum:
            return count
        
        return 0 
