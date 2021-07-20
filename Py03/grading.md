# Grading FPRO

Write a Python program that, given the four components of [the FPRO grade](https://web.fe.up.pt/~jlopes/doku.php/teach/fpro/sheet#calculation_formula_of_final_grade), by user input, returns the student's grade, an integer from 0 to 20, by using the formula:


grade = (LE + RE + 5 * PE + 3 * TE) / 50


The program returns:


* `"Input error"`, if the any of the components is not between 0 and 100
* `"RFC"`, if the PE < 40 or the TE < 40
* the grade as an integer, otherwise


*Careful:* There are many ways to round a number. You may want to avoid using `round()` since it uses "round half to even" but grades are rounded using "round half up". [[more](https://realpython.com/python-rounding/)]



## Private Tests [100%]

## Public Tests [100%]
