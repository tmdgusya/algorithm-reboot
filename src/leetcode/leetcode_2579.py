class Solution(object):
    def cal(self, prev, pointer, limit):
        if limit == 1:
            return 1
        acc = prev + 4 * (pointer - 1)
        if limit == pointer:
            return acc
        return self.cal(acc, pointer + 1, limit)

    def coloredCells(self, n):
        """
        :type n: int (positive number)
        :rtype: int
        """
        return self.cal(1, 1, n)
