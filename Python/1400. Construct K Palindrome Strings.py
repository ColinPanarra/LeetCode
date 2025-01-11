class Solution(object):
    def canConstruct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        if k==len(s):
            return True
        elif k>len(s):
            return False

        letter_map = {}
        odds = 0
        for letter in s: 
            if letter in letter_map:
                letter_map[letter] = letter_map[letter]+1
            else:
                letter_map[letter] = 1 
        
        for key, value in letter_map.items():
            if value%2 == 1:
                odds+=1
        if odds > k:
            return False
        return True
        



        
