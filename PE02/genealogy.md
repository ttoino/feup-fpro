# 5. Genealogy by group and order

The genealogy of somebody's family may be written in two forms:


* **Form 1:** `[("Ana", "sibling"), ("Carlos", "parent"), ("Diana", "parent")]`
* **Form 2:** `[(["Ana"], "sibling"), (["Carlos", "Diana"], "parent")]`


Write a Python function called `genealogy(l1)` that receives a genealogy list `l1` written in **Form 1** and returns a list written in **Form 2**.


The returned list must be ordered by relationship, using the following rule: *sibling < parent < cousin < grandparent*, and each sub-list must be ordered by *name*.



## Private Tests [100%]

## Public Tests [100%]
