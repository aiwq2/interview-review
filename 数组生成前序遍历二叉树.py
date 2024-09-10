class Node:
    def __init__(self,val,left=None,right=None) -> None:
        self.val=val
        self.left=left
        self.right=right

def preorder_traversal(root):
    if root is None:
        return []
    result = []
    result.append(root.val)
    result += preorder_traversal(root.left)
    result += preorder_traversal(root.right)
    return result

nums=[1,5,3,0,9,1]


index=0
def generate(nums):
    global index
    if  index>=len(nums) or nums[index]==0:
        return None
    
    root=Node(nums[index])
    index+=1
    root.left=generate(nums)
    index+=1
    root.right=generate(nums)
    return root

root=generate(nums)
result=preorder_traversal(root)
print(result)
