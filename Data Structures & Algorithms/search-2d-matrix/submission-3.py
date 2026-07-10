class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # use row major indexing to translate back and forth 
        # and map them to a 1d array and do binary search

        l = 0
        r = len(matrix)*len(matrix[0]) - 1

        while l <= r:
            mid = l + (r-l)//2

            # translate mid to row,col
            row = mid // len(matrix[0]) # divide by total cols
            col = mid % len(matrix[0]) # mod of total cols

            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                l = mid + 1
            else:
                r = mid - 1
        
        return False
