This program contains 6 functions and a logic tree that is used to provide the solutions for this specific problem.
6 functions are:
 fillA-Fill the jug A to 4 liters
 fillB-Fill the jug B to 4 liters
 frAB-Pour all the water from jug A to B
 frBA-Pour all the water from jug A to B
 porA-Pour out all the water from jug A to the ground
 porB-Pour out all the water from jug B to the ground
1 function tree
 checkanddo- This fuction provides a logical tree to the problem and tells what to do in every case scenario recursively
	     as it is called in each of the six functions called above.
Input:
There is no input required the program takes the initial conditions of the jugs as (0,0) or both are empty.

Output:
All possible list are prited in the first 255 rows
After that the total number of nodes are printed to reach every possible answer of the problem
The number of branches that lead to the answer (2,0) or Jug A is filled 2 lit and jug B is Empty is printed 
Classwjp.py
It is the implementation of water jug problems using classes