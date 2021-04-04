# Technojam-task_6
Complexity of a garland:
First thing that we need to understand is that the complexity of the garland is defined by number of pairs, of adjacent toys, which have different parity ie different remainder when divided by 2.
For example, the complexity of 1 4 2 3 5 is 2
1&4 have remainders 1&0 res,
4&2 have remainders 0&0 res,
2&3 have remainders 0&1 res,
3&5 have remainders 1&1 res.
So we have two pairs with different parity ie 2&3 and 1&4, hence complexity is 2.

When we create a program for the above problem we start with taking a variable for number of toys removed, then creating a matrix for storing and comparing the complexities of the adjacent pairs of toys,
zero is the removed toy so it is not taken into consideration.
