# 4. Isomorphic strings

Write a Python function `isomorphic(astring1, astring2)` that given two strings of the same length, determines if they are isomorphic. Two strings are called isomorphic if the characters in one string can be remapped to get the other string.


Remapping a character means replacing all occurrences of it with another character, while preserving the ordering of the characters. No two characters may map to the same character, but a character may map to itself. For example, the strings `"foo"` and `"app"` are isomorphic because it is possible to map `'f'` to `'a'` and `'o'` to `'p'`. The strings `"bar"` and `"foo"` are not isomorphic because it is not possible to map both `'a'` and `'r'` to `'o'`.


The function must return a properly formatted string:


`'<astring1>' and '<astring2>' are isomorphic because we can map: <alist>`


or


`'<astring1>' and '<astring2>' are not isomorphic`


if the strings are isomorphic or not, respectively. `<alist>` represents a list of tuples with all remapped characters between `astring1` and `astring2`. Notice that `<alist>` is ordered by the order of appearance in `<astring1>`.



## Private Tests [100%]

## Public Tests [100%]
