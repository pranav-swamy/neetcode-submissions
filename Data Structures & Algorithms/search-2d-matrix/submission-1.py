class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # row major indexing
        # binary search
        # need a way to convert a linear index to a 2d index

        left = 0
        right = len(matrix)*len(matrix[0]) - 1

        while left <= right:
            mid = left + (right - left) // 2
            row = mid // len(matrix[0]) # index // number of cols
            col = mid % len(matrix[0]) # index % number of cols
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return False
