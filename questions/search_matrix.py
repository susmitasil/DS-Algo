class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        
        for i in range(len(matrix)):
            start= 0
            end = len(matrix[i])-1
            if target>= matrix[i][start] and target<=matrix[i][end]:
                j = 0
                while j<len(matrix[i]):
                    if target == matrix[i][j]:
                        return True
                    
                    j+=1
                   
            
        return False         