def func_1(nums):
    """
    https://leetcode.com/problems/single-number/
    """
    set_1, set_2 = set(), set()
    for num in nums:
        if num in set_1:
            set_2.add(num)
        set_1.add(num)
    for i in (set_1 ^ set_2):
        return i


if __name__ == "__main__":
    nums = [4, 1, 2, 1, 2]
    print(func_1(nums))
