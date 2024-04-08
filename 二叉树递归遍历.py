class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def preorder_traversal(root):
    if root is None:
        return []
    result = []
    result.append(root.val)
    result += preorder_traversal(root.left)
    result += preorder_traversal(root.right)
    return result


def inorder_traversal(root):
    if root is None:
        return []
    result = []
    result += inorder_traversal(root.left)
    result.append(root.val)
    result += inorder_traversal(root.right)
    return result


def postorder_traversal(root):
    if root is None:
        return []
    result = []
    result += postorder_traversal(root.left)
    result += postorder_traversal(root.right)
    result.append(root.val)
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
