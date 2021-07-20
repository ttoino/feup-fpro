# 5. Number of patterns in a word

Write a Python function `subpatterns(astring)` that receives a string `astring` and computes the number of its substrings that follow a certain pattern.


The *pattern* is matched if the number of times that the substring *grows* is the same as the number of times the substring *shrinks*. A substring is *growing* at a particular character, if the character is bigger than the previous character, and is *shrinking* if it is smaller than the previous one. For example, `"ceda"` grows once (`'c'` < `'e'`) and shrinks twice (`'e'` > `'d'` and `'d'` > `'a'`). In this case, there's one substring pattern match (`"ce"` followed by `"ed"`).


The function returns a string with the same format as in the following examples.



## Private Tests [100%]

## Public Tests [100%]
