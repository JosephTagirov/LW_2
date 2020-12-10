nums = [1, 5, 3, 7, 4, 5]
import random


def qq(nums):
    if len(nums) <= 1:
        return nums
    else:
        q = random.choice(nums)
    l = [n for n in nums if n < q]

    e = [q] * nums.count(q)
    b = [n for n in nums if n > q]
    return qq(l) + e + qq(b)


print(qq(nums))
