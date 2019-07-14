def mkNode(tree1, value, tree2):
    return [tree1, value, tree2]

def mkLeaf():
    return []

def isLeaf(tree):
  return len(tree) == 0

def insert(x, tree):
    if isLeaf(tree):
        return mkNode(mkLeaf(), x, mkLeaf())

    left = tree[0]
    value = tree[1]
    right = tree[2]

    if x < value:
        return mkNode(insert(x, left), value, right)
    else:
        return mkNode(left, value, insert(x, right))

def bsearch(x, t):
    if isLeaf(t):
        return False

    left = t[0]
    value = t[1]
    right = t[2]

    if x == value:
        return True
    elif x < value:
        return bsearch(x, left)
    else:
        return bsearch(x, right)


tree = []
for i in [5, 4, 6, 3, 7, 2, 8, 1, 9, 0]:
    tree = insert(i, tree)

print(tree)

# print(bsearch(8, tree))
# print(bsearch(99, tree))
