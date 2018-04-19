import json
import unittest
n=8
def run(x):
	global board
	board=[[0 for i in range(n)] for j in range(n)] 
	inf=open(x)
	start=json.loads(inf.read())
	start=start["start"]
	if(start>7 or start<0):
		print("Invalid start position")
		return False
	board[start][0]=1;    #place queen in column 1 where specified
	if(place(1)==True):     #when solution found
		print("solution found")3++
		for i in board:
			print(i)
	else:
		print("solution not found")
	return True
class MyTestCases(unittest.TestCase):
	def test_positive(self):
    		self.assertEqual(run("input2.json"), True)
  	def test_negative(self):
                self.assertEqual(run("input3.json"), False)
def issafe(row,col):
	for i in range(n):
		for j in range(n):
			if(board[i][j]==1):
				if(row==i):
					return False
				if(col==j):
					return False
				if(abs(row-i)==abs(col-j)):
					return False
	return True
def place(col):
	if(col>=n):
		print("completed")
		return True
	for i in range(n):
		if(issafe(i,col)):
			board[i][col]=1     # queen placed here
			if(place(col+1)==True):     # place next queen
				return True
			board[i][col]=0       # backtrack, set to 0 
	return False
run("b1.json")
print("\n")
print "_____TESTING_____"
unittest.main()