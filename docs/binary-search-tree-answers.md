Knowledge Questions.

Question 1: In your own words, describe what a Binary Search Tree (BST) is.
In addition, describe two important properties of a BST: depth and height. How are they different?

-> A binary search tree is a type of binary tree where the nodes follow an ordered structure.
That is, for every node:

-All the nodes in its left subtree have values less than the node’s value.
-All the nodes in its right subtree have values greater than the node’s value.

-> A binary search tree's depth refers to the depth of its deepest node, where the depth of a node is defined by the number of 'connections' or 'lines' from that node to the root. 
-> A binary search tree's height refers to the number of 'connections' of the longest path from the root to a leaf, where a leaf is a node that does not have any children. 

Difference: When we refer to a node's depth, we're referring to the distance from that node to the root while if we refer to a node's height, we're measuring the distance from that node to the leaf. 

Question 2: In your own words, describe how an algorithm to find an item in a Binary Search Tree works.

-> To find an item in a binary tree, we do:
1. Start at the root, compare the target's value to the current node’s value (which is the root now) 
2. Based on the comparison, we have:
- If target equals current node value, then that is the target
- If target < current node value, move to the left child
- If target > current node value, move to the right child.
  Repeat this process for every node. 

3. If we reach a node where there is no child in the direction we want to go, the target is not in the tree.

Question 3: 
-> A balanced binary search tree, is a binary search tree where:
1. If we pick any node, its left and right subtrees' height should have a difference of no more than 1. 
2. If we pick any node, its left and right subtrees should also be balanced binary search trees

Question 8:
-> With the balanced binary search tree, because we pick the middle element as a root for every recursion, we basically cut down in half the pool of values for every resursion
- If we pick a tree with 1000 nodes, we have:
    Recursion steps
    1000 → 500
    500 → 250
    250 → 125
    125 → 63
    63 → 31
    31 → 15
    15 → 7
    7 → 3
    3 → 1
    1 → 0 (found or not found)
- That's 10 steps, and 10 is, roughly, log2 of 1000 so it would take at most log2(n) steps where n is the number of nodes. 