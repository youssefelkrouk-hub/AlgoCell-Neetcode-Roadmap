# there is library in python that let you count frquencies in an array : 

from collections import Counter
def LargestUniqueNumber(nums):
    counts=Counter(nums)
    return max((num for num, freq in counts.items() if freq == 1), default=-1)

