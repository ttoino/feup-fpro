# 5. Longest common prefix

Write a Python function `longest_prefix(words)` that, given a list of words called `words`, returns the longest common prefix to all the words.


For example, if `words = ["apple", "apply", "ape", "april"]`, then the biggest prefix is `"ap"`.


You should use the divide and conquer strategy to find out the longest prefix, as it is depicted in the figure:


xml version="1.0" encoding="UTF-8" standalone="no"?





Diagram



apple

apple



appl

appl



apple->appl





END

ap



appl->END





apply

apply



apply->appl





ape

ape



ap

ap



ape->ap





ap->END





april

april



april->ap






## Private Tests [100%]

## Public Tests [100%]
