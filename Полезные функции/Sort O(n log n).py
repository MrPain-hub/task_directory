# O(n*log(n)) сортировка
def merge(left, right):
    if len(left) == 0:
        return right
    if len(right) == 0:
        return left
    result = []
    index_l, index_r = 0, 0
    while len(result) < len(left) + len(right):
        if left[index_l] > right[index_r]:
            result.append(right[index_r])
            index_r += 1
        else:
            result.append(left[index_l])
            index_l += 1
        if index_l == len(left):
            result += right[index_r:]
            break
        if index_r == len(right):
            result += left[index_l:]
            break
    return result


def sort_log(lst):
    if len(lst) < 2:
        return lst
    median = len(lst)//2
    return merge(sort_log(lst[:median]), sort_log(lst[median:]))
