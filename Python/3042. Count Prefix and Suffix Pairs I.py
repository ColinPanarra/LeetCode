class Solution(object):
    def countPrefixSuffixPairs(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        ans=0
        length = len(words)
        for i in range(length-1):
            len_i= len(words[i])
         
            for j in range(i+1,length):
                j_word = words[j]
                len_j = len(j_word)

                if words[i] == j_word[:len_i] and words[i]==j_word[len_j-len_i:]:
                    ans+=1 
                
        return ans
