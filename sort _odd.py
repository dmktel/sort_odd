

def sort_odd(l):
    odds = sorted((i for i in l if i % 2 != 0))
    for index, item in enumerate(l):
        if item % 2 == 0:
            odds.insert(index, item)
    return odds

#Codewars best practices

def sort_array(arr):
  odds = sorted((x for x in arr if x%2 != 0), reverse=True)
  return [x if x%2==0 else odds.pop() for x in arr]