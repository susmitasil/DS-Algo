class Solution:
    def maxArea(self, height) -> int:
        l = 0
        h = len(height)-1
        val =0
        while l<h:
            mini = height[l] if height[l]<height[h] else height[h]
            temp = (h-l) * mini 
            if(temp> val):
                val= temp
                
            if height[l]<height[h]:
                l+=1
            else:
                h-=1
        return val

if __name__ == '__main__':
    area = Solution()
    print(area.maxArea([1,8,6,2,5,4,8,3,7]))
        