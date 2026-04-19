class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        height = len(matrix)
        width = len(matrix[0])
        if height * width < 3:
            if matrix[0][0] == target or matrix[-1][-1] == target:
                return True

        l, r = 0, height * width - 1
        i = 0
        while r > l:
            i += 1
            if i == 20:
                break
            middle = l + (r - l) // 2
            currentposition = matrix[middle // width][middle % width]
            if currentposition == target:
                return True
            if r - l == 1:
                currentposition2 = matrix[(middle + 1) // width][(middle + 1) % width]
                if currentposition2 == target:
                    return True
            if currentposition > target:
                r = middle
            else:
                l = middle
        return False