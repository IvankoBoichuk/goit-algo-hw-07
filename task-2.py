from utils import BST

tree = BST()
values = [20, 10, 30, 65, 15, 25, 35]
for val in values:
    tree.insert(val)

max_value = tree.find_min()
print("Найменше значення у дереві:", max_value)