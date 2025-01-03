
class Solution(object):
    def vowelStrings(self, words, queries):
        """
        :type words: List[str]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        words_values = []
        ans_list = [] 
      

        curr_sum = 0 
        for word in words:
            if word[0] in vowels and word[-1] in vowels:
                curr_sum+=1
            words_values.append(curr_sum)


        for x,y in queries:
            last_val = words_values[y] 
            first_val =  words_values[x-1]
            if x <= 0:
                ans_list.append(last_val)
            else:
                ans_list.append(last_val - first_val)

        return ans_list


