# 1. Collisions

In computer games, objects are typically approximated by a bounding box and collisions are computed efficiently by checking for intersections between these bounding boxes.


      image/svg+xml                   


Write a Python function `number_of_collisions(objects)` that returns the amount of collisions between each object given in the list `objects`.


Each object is a dictionary with the following keys: x1, x2, y1, y2, representing the top-left and bottom-right corner of the bounding box.


Hint: it is easier to write a function to check if two rectangles do **not** intersect than to check if they intersect.



## Private Tests [100%]

## Public Tests [100%]
