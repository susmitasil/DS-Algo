# Dynamic Programming

class Solution:
    def length_of_LIS(self, nums):
        LIS = [1]* len(nums)

        for i in range(len(nums)-1,-1,-1):
            print('check')
            for j in range(i+1, len(nums)):
                print(nums[i],nums[j])
                if nums[i]< nums[j]:
                    LIS[i]= max(LIS[i], 1+LIS[j])
                    print(LIS)

        return max(LIS)

if __name__=='__main__':
    lis = Solution()
    print(lis.length_of_LIS([0,1,0,3,2,3]))