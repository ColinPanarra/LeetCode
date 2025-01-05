class Solution(object):
    def shiftingLetters(self, s, shifts):
        """
        :type s: str
        :type shifts: List[List[int]]
        :rtype: str
        """
        #97 to 122
    
        shift_list = [0]*(len(s)+1)  # Convert string to a list for mutability
        s_list = []
        for start, end, direction in shifts:
            if direction == 0:
                shift_val = -1 
            else:
                shift_val=1
            shift_list[start]+=shift_val

            if(shift_list[end+1]<len(s)):
                shift_list[end+1]-=shift_val


        total_change = 0 
        for i, ch in enumerate(s):
            total_change+=shift_list[i]
            x = ord(ch)
            x= (x-97+total_change) % 26
            s_list.append(chr(x+97))
        
        return ''.join(s_list)

            

        

'''
INITIAL SOLUTION GOT Time Limit Exceeded 
        for start, end, direction in shifts:
            if direction == 0:
                shift_val = -1 
            else: 
                shift_val=1
            
            
            for i in range(start, end+1):
                c = s[i]
                c_val = ord(c)
                c_val+=shift_val
                if c_val<=96:
                    c_val=122
                if c_val>=123:
                    c_val=97
                new_c = chr(c_val)

                s = s[:i] + new_c + s[i+1:]

        return s 
    '''
