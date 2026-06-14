# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def __init__(self):
        self.paths = []

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.path(root,p,[])
        self.path(root,q,[])
        common_part = []
        l = min(len(self.paths[0]),len(self.paths[1]))
        i = 0
        while i < l and self.paths[0][i].val == self.paths[1][i].val:
            common_part.append(self.paths[0][i])
            i+=1

        return common_part[-1]
        

    def path(self,start,end,path):
        if start == None:
            return

        if start.val == end.val:
            self.paths.append(path + [end])
            return 

        self.path(start.left,end,path+[start])
        self.path(start.right,end,path+[start])
        return 
