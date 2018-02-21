from memoize import memoize

@memoize
def knapsack(items, max_weight):
    if len(items) == 0 or max_weight <= 0:
        return 0

    first = items[0]
    rest = items[1:]

    # Don’t include the first item
    value_without_first = knapsack(rest, max_weight)

    # Include the first item
    if first.weight <= max_weight:
        value_with_first = knapsack(rest, max_weight - first.weight) + first.value
        return max(value_with_first, value_without_first)
    else:
        return value_without_first

class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value

items = (Item(12, 4), Item(2, 2), Item(1, 2), Item(1, 1), Item(4, 10)) # Solution: Value=15
max_weight = 15
print(knapsack(items, max_weight))
