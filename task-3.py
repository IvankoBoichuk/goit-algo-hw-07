from utils import BST

tree = BST()
values = [20, 10, 30, 5, 15, 25, 35]
for val in values:
    tree.insert(val)

total_sum = tree.sum_values()
print("Сума всіх значень у дереві:", total_sum)