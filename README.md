This project was developed to solve Sudoku problems presented in a HackerRank challenge.
The primary task is to solve multiple Sudokus provided as input.
I used linear regression as the method to solve the puzzles, and the code successfully passed all the challenges.
However, the time taken to solve the problems is something I aim to improve in the future.

Input

The first line contains N which is the number of Sudoku puzzles. N Sudoku puzzles follow. 
Each one contains 9 lines with each line containing 9 space separated integers. 
A 0 indicates an unfilled square, and an integer between 1 and 9 denotes a filled square with that value.

Sample Input

2
0 0 0 0 0 0 0 0 0
0 0 8 0 0 0 0 4 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 6 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
2 0 0 0 0 0 0 0 0
0 0 0 0 0 0 2 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 8 0 0 0 0 4 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 6 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
2 0 0 0 0 0 0 0 0
0 0 0 0 0 0 2 0 0
0 0 0 0 0 0 0 0 0

Output

Output to STDOUT the completely filled Sudoku board for each Sudoku. If there are multiple solutions, you can output any one.
