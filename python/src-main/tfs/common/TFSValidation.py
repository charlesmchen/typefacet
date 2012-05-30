'''
robofont-extensions-and-scripts
TFSValidation.py

https://github.com/charlesmchen/robofont-extensions-and-scripts

Copyright (c) 2012 Charles Matthew Chen
charlesmchen@gmail.com


'''



'''
We have the following constraints on input:

    * Every contour has at least one edge.
    * Every contour is "closed" (ie. has the same start point and end point.)
    * Every edge is a straight line, quadratic bezier or cubic bezier.
    * Every point in a edge is valid (ie. not NaN or Inf).
    * Every contour is a "shape" or a "hole."
    * Every "hole" is entirely contained within one "shape."
    * A "shape" may contain more than one "hole."
    * No two contours share an edge.  That includes colinear edges with separate endpoints.

       ....
       .  .
     ..X  . The two shapes do not share any endpoints but have colinear edges. Invalid.
     . X  .
     ..X  .
       .  .
       ....

    * Two "shape" contours may share an endpoint.
    * Two "hole" contours may share an endpoint.
    * The endpoint of "shape" may be colinear with the edge of another "shape."
    * The endpoint of "hole" may be colinear with the edge of another "hole."
    * A "shape" and a "hole" may not share an endpoint, nor may any endpoint of an "edge" be colinear
      with the edge of the "shape" it contains.
    * No contour intersects/crosses itself.
    * No contour has two colinear and overlapping edges, even if they have separate endpoints.
    * A contour may use the same endpoint more than once, like so:

    .....
    .   .
    . ..X...
    . . .  . The contour visits point X twice.
    . ...  .
    ........

    * Ideally, shapes will have clockwise orientation and holes have counter-clockwise orientation.
       * I don't think we're going to enforce this requirement on our inputs.
         We'll normalize our inputs to this condition instead.
    * TODO: what other forms of degenerate geometry are invalid?  What about precision?

'''
