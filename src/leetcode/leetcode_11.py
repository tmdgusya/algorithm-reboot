import unittest


def maxArea(height):
    """
    :type height: List[int]
    :rtype: int
    """
    answer = 0
    for i in range(len(height) - 1):
        p1 = i
        h1 = height[i]
        for j in range(i + 1, len(height)):
            p2 = j
            h2 = height[j]
            width = p2 - p1
            h = min(h1, h2)
            result = width * h
            answer = max(answer, result)
    return answer

def maxArea2(height):
    L, R = 0, len(height) - 1
    answer = 0
    while L < R:
        width = R - L
        h = min(height[L], height[R])
        result = width * h
        answer = max(answer, result)
        if height[R] > height[L]:
            L += 1
        else:
            R -= 1
    return answer

class MyTestCase(unittest.TestCase):
    def test_one(self):
        result = maxArea2([1,8,6,2,5,4,8,3,7])
        self.assertEqual(49, result)


if __name__ == '__main__':
    unittest.main()
