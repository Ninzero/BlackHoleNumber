# BlackHoleNumber
All the code about how to find black hole numbers using Python.
## Version1.0
The basic way to find black numbers, slow.
## Version1.1
Randomly pick 100000 numbers to estimate time needed in Version1.0.
## Version2.0
Try to avoid repeated calculation. But because

> elif num in calculated

need to compare every number in calculated with "num", actually much slower then Version1.0.
## Version2.1
Using binary search to check whether "num" is in "calculated". But need to sort "calculated" every time add number in, even slower than Version2.0.
## Version2.2
Using binary search both to check whether in "calculated" but also where to add "num" so that the list will alway be sorted and can use binary search. Save 72% of the time based on time needed for six-digit black hole number using Version1.0.
## Version2.3
Using *dict* as ordered set, same principle but different realization, save 90% of the time based on time needed for six-digit black hole number using Version1.0.
## Version3.0
Use the method **Riddle** to avoid "equal" numbers in the situation of finding black hole numbers. Save 1% more than Version2.3.
## Version3.1
Using a generator to directly generate "candidates" for search. And effectively lower the time  needed for searchinSmall changes
