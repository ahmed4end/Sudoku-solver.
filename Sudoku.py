class Sudoku():
	def __init__(self, matrix, show=True, check_validation=False):
		self.matrix = matrix
		self.solve()
		if show:print(matrix)
		if check_validation:print(self.check(self.matrix))

	def predict(self, matrix):#predictor of the valid values of every 0s cells in the matrix. 
		subgrids = { (x,y):j for x, i in enumerate([[[matrix[y+i][x+j] for i in (-1,0,1) for j in (-1,0,1)] for x in range(1,9,3)] for y in range(1,9,3)]) for y, j in enumerate(i)}
		nums = { (x,y):j for x, i in enumerate(matrix) for y, j in enumerate(i)}
		valids = {i:list(set(range(1,10))-set(subgrids[(i[0]//3, i[1]//3)])-set(matrix[i[0]])-set(list(zip(*matrix))[i[1]])-set([nums[i],0])) for i in nums.keys() if nums[i] == 0}
		return valids

	def solve(self):          #solver, it works using (backtracking)&recursion.
		raw_gaps = self.predict(self.matrix)
		if len(raw_gaps) == 0:return True
		gap, valids= next(iter(raw_gaps.keys())), next(iter(raw_gaps.values()))
		for i in valids:
			self.matrix[gap[0]][gap[1]] = i
			if self.solve():return True
			self.matrix[gap[0]][gap[1]] = 0
		return False

	def check(self, matrix):#sudoku matrix validation checker.
		return all([set(range(1,10))-set([matrix[y+i][x+j] for i in (-1,0,1) for j in (-1,0,1)])==set() for y in range(1,9,3) for x in range(1,9,3)]+[set(range(1,10))-set(i)==set() for i in matrix+list(zip(*matrix))])

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
	Sudoku(sudoku)

