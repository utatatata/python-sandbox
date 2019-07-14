def merge(ls):
    if len(ls) <= 1:
        return ls

    m = len(ls) // 2
    xs = merge(ls[:m])
    ys = merge(ls[m:])

    rs = []
    while len(xs) != 0 or len(ys) != 0:
        if len(xs) == 0:
            rs.append(ys.pop(0))
        elif len(ys) == 0:
            rs.append(xs.pop(0))
        elif xs[0] < ys[0]:
            rs.append(xs.pop(0))
        else:
            rs.append(ys.pop(0))
    return rs


print(merge([4, 3, 1, 2]))
print(merge([5, 1, 2, 6, 4, 3]))
print(merge([1, 8, 3,3,3, 6, 5, 4, 3, 7, 2]))
print(merge([3, 2, 1, 4]))


