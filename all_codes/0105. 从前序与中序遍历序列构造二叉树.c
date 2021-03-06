// 根据一棵树的前序遍历与中序遍历构造二叉树。
//
// 注意:
// 你可以假设树中没有重复的元素。
//
// 例如，给出
//
// 前序遍历 preorder = [3,9,20,15,7]
// 中序遍历 inorder = [9,3,15,20,7]
// 返回如下的二叉树：
//
//     3
//    / \
//   9  20
//     /  \
//    15   7
//
// 来源：力扣（LeetCode）
// 链接：https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal
// 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

struct TreeNode* buildTree(int* preorder, int preorderSize, int* inorder, int inorderSize){
    if(preorderSize != inorderSize || preorderSize <= 0 || inorderSize <=0)
        return NULL;
    
    struct TreeNode* tree;
    tree = (struct TreeNode*)malloc(sizeof(struct TreeNode));
    tree->val = preorder[0];
    
    // i表示左子树节点数量
    int i = 0;
    for(; i <= inorderSize; i++)
        if(inorder[i] == preorder[0])
            break;

    tree->left = buildTree((preorder+1), i, inorder, i);
    tree->right = buildTree((preorder+1+i), preorderSize-1-i, (inorder+i+1), inorderSize-1-i);
    return tree;
}
