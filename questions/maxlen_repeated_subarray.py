class Solution(object):
        def findLength(self, A, B):
            dp = [[0] * (len(B)+1) ] * (len(A)+1)
            max_count = 0
            for i in range(len(A)):
                for j in range(len(B)):
                    if(A[i] == B[j]):
                        dp[i][j] = dp[i-1][j-1]+1
                        max_count = max(max_count,dp[i][j])
            return max_count

ob = Solution()
print(ob.findLength([1,2,3,2,1,4],[3,2,1,4,2]))