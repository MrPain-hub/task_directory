from re import search
from icecream import ic


def translate_time(data):
    """
    перевод к минутам
    """
    hour, minute = map(int, data[:-2].split(":"))
    if hour == 12:
        hour = 0
    zone = data[-2:]
    all_minute = hour * 60 + minute
    if zone == "pm":
        all_minute += 12 * 60
    return all_minute


def difference_time(t_1, t_2, time_min):
    """
    Вычисление и сравнение
    """
    if abs(t_2 - t_1) < time_min:
        return abs(t_2 - t_1)
    if (t_2 + t_1) % (24 * 60) < time_min:
        return (t_2 + t_1) % (24 * 60)
    if (24 * 60) % (t_2 + t_1) < time_min:
        return (24 * 60) % (t_2 + t_1)
    return time_min


def difference_time_1(t_1, t_2, time_min):
    """
    Вычисление и сравнение
    """
    all_sum = t_2 + t_1
    if all_sum > 24 * 60:
        all_sum = all_sum - 24 * 60
    if all_sum > 12 * 60:
        if t_2 > t_1:
            all_sum = abs((24 * 60 + t_1) - t_2)
        else:
            all_sum = abs((24 * 60 + t_2) - t_1)
    if abs(t_2 - t_1) < all_sum:
        all_sum = abs(t_2 - t_1)
    if all_sum < time_min:
        return all_sum
    return time_min


strArr = ["10:00am", "11:45pm", "5:00am", "12:01am"]
time_min = 24 * 60


for i in range(len(strArr)):
    t_1 = translate_time(strArr[i])
    for element in strArr[:i]:
        t_2 = translate_time(element)
        time_min = difference_time_1(t_1, t_2, time_min)
    for element in strArr[i + 1:]:
        t_2 = translate_time(element)
        time_min = difference_time_1(t_1, t_2, time_min)
print(time_min)



lst = ["11:45pm", "12:01am"]
x1 = translate_time(lst[0])
x2 = translate_time(lst[1])
ic(x1, x2)
ic(difference_time_1(x1, x2, 24*60))

lst = ["1:10pm", "5:00pm"]
x1 = translate_time(lst[0])
x2 = translate_time(lst[1])
ic(x1, x2)
ic(difference_time_1(x1, x2, 24*60))


text = "fdfdf"
print(text[:4] + text[:4])
