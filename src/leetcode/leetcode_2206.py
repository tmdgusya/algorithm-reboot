class Solution(object):
    def divideArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool

        The elements present in a pair are equal
        (2,2)

        we gonna make an frequency map if the frequency of numbers are not divided by 2, then return False
        """
        frequency = {}

        for n in nums:
            c = frequency.get(n, 0)
            frequency[n] = c + 1

        # validate
        for n in nums:
            if frequency[n] % 2 != 0:
                return False

        return True
        