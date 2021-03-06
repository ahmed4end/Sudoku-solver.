def solve(sudoku): #using recursion and backtracking, here we go.
	empties = [(i,j) for i in range(9) for j in range(9) if sudoku[i][j] == 0]                       #this step detects the empty cells to fill it later.
	predict = lambda i, j: set(range(1,10))-set([sudoku[y+range(1,10,3)[i//3]][x+range(1,10,3)[j//3]] for y in (-1,0,1) for x in (-1,0,1)])-set(sudoku[i])-set(list(zip(*sudoku))[j])                       #this lambda function predicts all valid values for a certain cell.
	if len(empties)==0:return True                                                                   #recursion's endline trigger to avoid infinite loops (triggered when all cells are filled.).
	gap = empties[0]                                                                     
	predictions = predict(*gap)
	for i in predictions:
		sudoku[gap[0]][gap[1]] = i
		if solve(sudoku):return True
		sudoku[gap[0]][gap[1]] = 0
	return False    

def check(sudoku): #extra function to check solution if correct or wrong :"D
	return all([set(range(1,10))-set([sudoku[y+i][x+j] for i in (-1,0,1) for j in (-1,0,1)])==set() for y in range(1,9,3) for x in range(1,9,3)]+[set(range(1,10))-set(i)==set() for i in sudoku+list(zip(*sudoku))])

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

	
