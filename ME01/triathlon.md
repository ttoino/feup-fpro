# 4. Triathlon

In a triathlon competition, there are 3 stages: 1.5 km of swimming, 40 km of cycling and, finally, 10 km of running. Each participant must complete all three under 4 hours and must have a minimum velocity of 2 km/h in the swimming stage, 20 km/h in cycling and 8 km/h in running.


Write a Python program that, given three times of completion `tS`, `tC` and `tR` (in hours; one for each stage) by user input, in this order, checks if the participant met all the requirements. If so, it should print the total time. Otherwise, it should print the first factor that caused the disqualification (“Time”, “Swimming”, “Cycling” or “Running”, in this order).


For example:


* for tS=`0.4`, tC=`1.2`, tR=`0.4`, the output is: `2.0` (the total time)
* for tS=`1`, tC=`1`, tR=`4`, the output is: `Time`
* for tS=`0.5`, tC=`1`, tR=`2.2`, the output is: `Running`



## Private Tests [100%]

## Public Tests [100%]
