

def sort_odd(l):
    odds = sorted((i for i in l if i % 2 != 0))
    for index, item in enumerate(l):
        if item % 2 == 0:
            odds.insert(index, item)
    return odds

print(sort_odd([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]))