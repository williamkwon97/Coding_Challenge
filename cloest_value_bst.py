class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def closestValue(root, target):
    # write your code here
    closest = root.val
    print("closest-", closest)

    while root:
        print("root.val-", root.val)
        closest = root.val if abs(root.val - target) < abs(closest -
                                                           target) else closest
        if target > root.val:
            root = root.right
        else:
            root = root.left
    return closest


root = TreeNode(8)
root.left = TreeNode(5)
root.right = TreeNode(14)
root.left.left = TreeNode(4)
root.left.right = TreeNode(6)
root.left.right.left = TreeNode(8)
root.left.right.right = TreeNode(7)
root.right.right = TreeNode(24)
root.right.right.left = TreeNode(22)

result = closestValue(root, 19)
print(result)