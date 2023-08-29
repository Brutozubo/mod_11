a = [4, 5, 6, 10, 1, 3]

def merge_sort(a):
    if len(a) < 2:
        return a[:]
    else:
        median = int(len(a) / 2)
        left = merge_sort(a[:median])
        right = merge_sort(a[median:])
        return merge(left, right)

def merge(left, right):
    res = []
    i, j = 0, 0
    while i < len(left) and j < len (right):
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    while i < len(left):
        res.append(left[i])
        i += 1
    while j < len(right):
        res.append(right[j])
        j += 1
    return res

print(merge_sort(a))



import unittest

class TestMergeSort(unittest.TestCase):
    def test_normal_merge(self):
        left = [4, 5, 6]
        right = [10, 1, 3]
        out = [4, 5, 6, 10, 1, 3]
        self.assertEqual(merge(left, right), out)

    def test_right_empty(self):
        left = [4, 5, 6]
        right = []
        out = [4, 5, 6]
        self.assertEqual(merge(left, right), out)

    def test_left_empty(self):
        left = []
        right = [10, 1, 3]
        out = [10, 1, 3]
        self.assertEqual(merge(left, right), out)

if __name__ == "__main__":
    unittest.main()

