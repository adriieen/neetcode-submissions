class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        nums_c = [(i,nums[i]) for i in range(len(nums))]
        nums_c.sort(key=lambda x: x[1])

        i1, i2 = 0, len(nums)-1
        while nums_c[i1][1]+ nums_c[i2][1] !=target:
            sum = nums_c[i1][1]+ nums_c[i2][1]
            if sum<target:
                i1+=1
            else :
                i2-=1
        idx1, idx2 = nums_c[i1][0],nums_c[i2][0]
        
        return([idx1,idx2] if idx1<idx2 else [idx2,idx1])