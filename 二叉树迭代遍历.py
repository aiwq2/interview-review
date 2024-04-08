class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def preorder_traversal(root):
    if root is None:
        return []
    stack = [root]
    result = []
    while stack:
        node = stack.pop()
        result.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return result


def inorder_traversal(root):
    if root is None:
        return []
    stack = []
    result = []
    node = root
    while node or stack:
        while node:
            stack.append(node)
            node = node.left
        node = stack.pop()
        result.append(node.val)
        node = node.right
    return result


def postorder_traversal(root):
    if root is None:
        return []
    stack = [root]
    result = []
    while stack:
        node = stack.pop()
        result.append(node.val)
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    return result[::-1]


def level_order_traversal(root):
    if root is None:
        return []
    stack = [root]
    result = []
    while stack:
        node = stack.pop(0)
        result.append(node.val)
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    return result


# 创建二叉树
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# 前序遍历
print("前序遍历结果：", preorder_traversal(root))

# 中序遍历
print("中序遍历结果：", inorder_traversal(root))

# 后序遍历
print("后序遍历结果：", postorder_traversal(root))

# 层序遍历
print("层序遍历结果：", level_order_traversal(root))
