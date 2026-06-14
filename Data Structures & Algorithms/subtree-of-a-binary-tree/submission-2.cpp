/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
public:
    bool isSubtree(TreeNode* root, TreeNode* subRoot) {
        if (root == nullptr) return false;  // Ran out of tree to search

        if (sameTree(root, subRoot)) return true;  // Match found at this node

        // Otherwise, check left and right subtrees
        return isSubtree(root->left, subRoot) || isSubtree(root->right, subRoot);
        
    }

    bool sameTree(TreeNode* root1, TreeNode* root2){
        if (root1 == nullptr && root2 == nullptr) {
            return true;
        }

        if( root1 == nullptr && root2 != nullptr) {
            return false;
        }

        if(root1 != nullptr && root2 == nullptr) {
            return false;
        }

        if (root1->val != root2->val) {
            return false;
        }

        return sameTree(root1->left,root2->left) && sameTree(root1->right,root2->right);
    }
};
