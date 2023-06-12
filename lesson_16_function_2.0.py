#Task_1
def change(lst):
    lst[0], lst[-1] = lst[-1], lst[0]
#Task_2
def to_dict(lst):
    return {item: item for item in lst}

#Task_3
def sum_range(start, end):
    if start > end:
        start, end = end, start

    return sum(range(start, end + 1))
