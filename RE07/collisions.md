# 2. Hash Collisions

Consider a collection of documents, where each document is associated to a numerical *hash*. When two documents have the same hash, there is a *hash collision*; this needs to be detected and avoided.


Write a Python function called `collisions(alist)` that receives a list of positive integers `alist` and returns a dictionary with the frequency of the hash associated to each element in the list. As the hash function, use the modulus-8 of the sum of the digits in the number. For example, if the number is 24 then the hash is 6 (because (2 + 4) % 8 = 6).


Note that two dictionaries `d1` and `d2` are considered equal (`d1 == d2`), even if the keys' order is different as long as `d1.items() == d2.items()`. Therefore the order of your returned dictionary is not important.



## Private Tests [100%]

## Public Tests [100%]
