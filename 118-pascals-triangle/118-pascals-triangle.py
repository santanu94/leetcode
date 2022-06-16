class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        prev_left = prev_right = 0
        result = []
        
        for i in range(numRows):
            row = []
            for j in range(i+1):
                if j == 0:
                    prev_left = 0
                    prev_right = 1
                elif j == i:
                    prev_left = 1
                    prev_right = 0
                else:
                    prev_left = result[i-1][j-1]
                    prev_right = result[i-1][j]
                
                row.append(prev_left + prev_right)
            
            result.append(row)
        
        return result
                
            