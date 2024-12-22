class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)<=1:
            return len(nums)

        checked = sorted(set(nums))
        x=0

        for num in checked:
            nums.insert(x,num)
            x+=1
        
        return len(checked)

        
