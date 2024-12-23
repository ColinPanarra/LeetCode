class Solution(object):
    def isPrefixOfWord(self, sentence, searchWord):
        """
        :type sentence: str
        :type searchWord: str
        :rtype: int
        """
        if searchWord not in sentence:
            return -1
        
        else:
            x=1
            for word in sentence.split(' '): 
                if searchWord in word[0:len(searchWord)]:

                    return x
                else:
                    x+=1

        return -1
        
