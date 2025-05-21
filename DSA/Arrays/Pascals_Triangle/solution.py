'''Pascal's triangle. This solution got me 100% in Runtime and the runtime was
0 ms- beats 100%. Can you believe it? The algorithm is pretty simple, unless
the element under consideration is on the edge of the triangle, go to the last
appended row in the triangle, for the given index, add [i-1]th and [i]th element
and that's your [i]th element of the row being made.
This solution was made with Anirudh Kannan on May 22nd, at 12:30 AM at night
during a workday. Hope this works out for the best.
There is a solution that uses nCr, it's in solution_2.

Link to the problem statement: https://leetcode.com/problems/pascals-triangle/ '''


class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        triangle = [[1]]
        for i in range(1,numRows):
            row=[1]
            for j in range(1,i):
                row.append(triangle[-1][j-1]+triangle[-1][j])
            row.append(1)
            triangle.append(row)
        return triangle        