# 1. List manipulation

Consider the following set of commands:




| Command | Description |
| --- | --- |
| **insert i e** | Insert integer **e** at position **i** |
| **print** | Save list to result string |
| **remove e** | Delete the first occurrence of integer **e** |
| **append e** | Insert integer **e** at the end of the list |
| **sort** | Sort the list in ascending order |
| **pop** | Remove the last element from the list |
| **reverse** | Reverse the list |


Write a Python function `manipulator(l, cmds)` that, given a list of commands as a list of strings `cmds`, applies them sequentially to a list `l` and **returns a string** which contains the result of all print commands (separated by a single space).


You can assume all command arguments are valid (e.g. insertion index is valid and remove specifies an element that exists in the list at that time).



## Private Tests [100%]

## Public Tests [100%]
