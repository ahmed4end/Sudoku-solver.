def solve(sudoku):
	#using recursion and backtracking, here we go.
	empties = [(i,j) for i in range(9) for j in range(9) if sudoku[i][j] == 0]
	predict = lambda i, j: set(range(1,10))-set([sudoku[i][j]])-set([sudoku[y+range(1,10,3)[i//3]][x+range(1,10,3)[j//3]] for y in (-1,0,1) for x in (-1,0,1)])-set(sudoku[i])-set(list(zip(*sudoku))[j])
	if len(empties)==0:
		return True
	gap = next(iter(empties))
	predictions = predict(*gap)
	for i in predictions:
		sudoku[gap[0]][gap[1]] = i
		if solve(sudoku):
			return True
		sudoku[gap[0]][gap[1]] = 0
	return False

if __name__ == "__main__":
	sudoku = [[0,0,0,6,0,1,0,0,0], 
	   	  [0,0,4,5,0,7,2,0,0], 
	          [1,0,3,0,0,0,7,0,6], 
	          [0,5,0,9,0,3,0,8,0], 
	          [3,0,0,0,8,0,0,0,9], 
	          [2,8,0,0,5,0,0,7,3], 
	          [5,0,0,7,0,8,0,0,1], 
	          [0,4,0,2,0,5,0,6,0], 
	          [0,0,2,3,0,4,8,0,0]]
	solve(sudoku)
	print(sudoku)
