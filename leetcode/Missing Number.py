def func_1(nums):
    """
    https://leetcode.com/problems/missing-number/
    """
    set_1 = set(nums)
    set_2 = set(range(len(nums) + 1))

    out = set_2 ^ set_1
    for i in out:
        return i


def func_2(nums):
    """
    https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
    """
    set_1 = set(nums)
    set_2 = set(range(1, len(nums) + 1))

    set_out = set_2 ^ set_1
    lst_out = []
    for i in set_out:
        lst_out.append(i)
    return lst_out


if __name__ == "__main__":
    nums = [4,3,2,7,8,2,3,1]
    print(func_2(nums))
