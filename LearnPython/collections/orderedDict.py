from collections import OrderedDict

ordered_dictionary = OrderedDict()
for _ in range(int(input())):
    item, space, price = input().rpartition(' ')
    ordered_dictionary[item] = ordered_dictionary.get(item, 0) + int(price)
for item, price in ordered_dictionary.items():
    print(item, price)
    