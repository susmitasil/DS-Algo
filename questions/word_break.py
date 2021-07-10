class Solution:
    def wordBreak(self, s:str,wordDict ) -> bool:
        
        dp = [True] + [False]*len(s) 

        for i in range(1,len(s)+1):
            for w in wordDict:
                if dp[i-len(w)] and s[(i-len(w)):i] == w:
                    dp[i] = True
        print(dp[-1])
        return(dp[-1])

if __name__=='__main__':
    wb = Solution()
    wb.wordBreak("leetcode", ["leet","code"])
    wb.wordBreak("catsandog", ["cats","and","sand","dog","cat"])
    wb.wordBreak("applepenapple", ["apple","pen"])
    wb.wordBreak("ccccccc", ["ccccc","ccc"])