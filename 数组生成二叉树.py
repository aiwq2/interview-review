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
def generate_preorder(nums):
    global index
    if  index>=len(nums) or nums[index]==0:
        return None
    
    root=Node(nums[index])
    index+=1
    root.left=generate_preorder(nums)
    index+=1
    root.right=generate_preorder(nums)
    return root

def generate_cengxu(nums,index):
    if index>=len(nums) or nums[index]==0:
        return None
    root=Node(nums[index])
    root.left=generate_cengxu(nums,2*index+1)
    root.right=generate_cengxu(nums,2*index+2)
    return root

# root=generate_preorder(nums)
root=generate_cengxu(nums,0)
result=preorder_traversal(root)
print(result)
