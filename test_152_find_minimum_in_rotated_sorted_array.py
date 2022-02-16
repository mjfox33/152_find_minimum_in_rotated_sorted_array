from code_152_find_minimum_in_rotated_sorted_array import Solution

def test_example_1():
    s = Solution()
    assert s.findMin2([3,4,5,1,2]) == 1

def test_example_2():
    s = Solution()
    assert s.findMin2([4,5,6,7,0,1,2]) == 0

def test_example_3():
    s = Solution()
    assert s.findMin2([11,13,15,17]) == 11