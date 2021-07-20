# 3. Binary tree

Binary trees can be used to make it fast to search for unidimensional information. In this data structure, each parent can have two children (left and right) which are also binary trees.


Consider the following binary tree:


xml version="1.0" encoding="UTF-8" standalone="no"?





BST



F: 1

F: 1



B: 10

B: 10



F: 1->B: 10




X: 20

X: 20



F: 1->X: 20




A: 50

A: 50



B: 10->A: 50




C: 35

C: 35



B: 10->C: 35




null0




X: 20->null0




null1




X: 20->null1




null2




A: 50->null2




null3




A: 50->null3




null4




C: 35->null4




null5




C: 35->null5




Each node is represented by a tuple of the form `(key, contents, left, right)`. The key values of the nodes to the *left* are smaller than the parent key value and to the *right* are bigger than the parent key value. These two nodes are represented by functions that must be called to return the rest of the tree.


Write a function `binary_tree(key, tree)` that, given a string as `key` and the first node as `tree`, returns the corresponding contents. The key always exists in the tree.


Take advantage of the binary structure of the tuple, to iterate the tree in as few iterations as possible. If you go through a path that is not the shortest, then the function will be `lambda: 1/0` 💣.



## Private Tests [100%]

## Public Tests [100%]
