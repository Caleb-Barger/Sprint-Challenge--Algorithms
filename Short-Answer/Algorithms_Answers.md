#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n)


b) O(n^2)


c) O(nlogn) ?

## Exercise II
given n story building, at f floor or higer dropping eggs will break
dropping eggs one floor lower than f however will not break the egg
how can we find the floor where dropped + broken eggs is low!

To minimize eggs broken we would check the middle floor first (if it is odd num just round down), if the egg does not break than we 
know that f = mid + 1, otherwise we now have 2 sections (branches) where f floor could be (everything below mid & everything above mid + 1)
now that we have broken the possible locations of floor f into 2 parts we can then delegate the work of locating floor f
by recursivly calling this function... eventually one of the functions will hit our first if statement and pass the location of floor f
back up the call stack and we can come back with an answer with a runtime of O(logn) because we are gaining info as we try finding f




