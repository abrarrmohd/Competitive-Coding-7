"""
Approach: Binary search on the range of numbers present in the matrix
t.c. => O(n^2log(max - min)) where n = len(row)
s.c. => O(1)
"""
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        l, r = matrix[0][0], matrix[n - 1][n - 1]
        while l <= r:
            mid = l + (r - l)//2
            less, equal = self.getCount(mid, n, matrix)
            numElements = less + equal

            if equal > 0 and less + 1 <= k <= numElements:
                return mid
            elif numElements < k:
                l = mid + 1
            else:
                r = mid - 1
        return -1

    def getCount(self, mid, n, matrix):
        less, equal = 0, 0
        for i in range(n):
            j = n - 1
            while j >= 0 and matrix[i][j] >= mid:
                if matrix[i][j] == mid:
                    equal += 1
                j -= 1
            less += (j + 1)
        return less, equal