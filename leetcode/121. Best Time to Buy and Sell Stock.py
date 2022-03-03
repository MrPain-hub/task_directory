def func_1(nums):
    """
    https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
    """
    sell = nums.pop()
    profit = 0
    while len(nums) > 0:
        price = nums.pop()
        if sell < price:
            sell = price
        else:
            if profit < sell - price:
                profit = sell - price
    return profit


if __name__ == "__main__":
    x = [7,1,5,3,6,4]
    print(func_1(x))

