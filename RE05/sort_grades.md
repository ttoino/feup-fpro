# 5. Students grades

Consider student records, given as a nested tuple of N tuples in the format *(name, number, (grade\_1, grade\_2, ...))*.  Write a Python function `sort_grades(records)` to sort the student records according to the following criteria:


1. Sort based on the average grade (descending order);
2. Then sort based on student name (ascending order);
3. Then sort based on student number (ascending order);


where *name* and *number* are strings, and each *grade* is an integer between 0 and 100.


Hint: For sorting, you should use the built-in function `sorted()`, in which you can define your own *key-sorting* function.



## Private Tests [100%]

## Public Tests [100%]
