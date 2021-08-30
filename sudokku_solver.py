#For solving and checking sudoku

import os
#_____________________________________________________solving_______________________________________________________________________
def print_grid(arr): 
	for i in range(9): 
		for j in range(9): 
			print (arr[i][j],end=" ") 
		print ('\n') 

def find_empty_location(arr,l): 
	for row in range(9): 
		for col in range(9): 
			if(arr[row][col]==0): 
				l[0]=row 
				l[1]=col 
				return True
	return False

def used_in_row(arr,row,num): 
	for i in range(9): 
		if(arr[row][i] == num): 
			return True
	return False 

def used_in_col(arr,col,num): 
	for i in range(9): 
		if(arr[i][col] == num): 
			return True
	return False

def used_in_box(arr,row,col,num): 
	for i in range(3): 
		for j in range(3): 
			if(arr[i+row][j+col] == num): 
				return True
	return False 

def check_location_is_safe(arr,row,col,num):  
	return not used_in_row(arr,row,num) and not used_in_col(arr,col,num) and not used_in_box(arr,row - row%3,col - col%3,num) 

def solve_sudoku(arr): 	 
	l=[0,0]  
	if(not find_empty_location(arr,l)): 
		return True

	row=l[0] 
	col=l[1] 
	 
	for num in range(1,10): 
		if(check_location_is_safe(arr,row,col,num)): 
			arr[row][col]=num 
			if(solve_sudoku(arr)): 
				return True
			arr[row][col] = 0		 
	return False
 
def solve():	
	grid=[]
	print("enter sudoku for solving \n enter 0 for blank spaces")
	for i in range(9):
	  l=list(map(int,input().split()))
	  grid.append(l)

	if(solve_sudoku(grid)):
		print_grid(grid)
	else: 
		print ("No solution exists") 




#____________________________________________________________checking________________________________________________________________
 
def chcol(a,p):
    
    q=0
    for i in range(9):
        d={}
        for j in range(9):
            flage=0
            if a[j][i] not in d:
                d[a[j][i]]=((i+1)*10)+(j+1)
                flage=1
            if flage==0:
                q=1
                if (((i+1)*10)+j+1) not in p:
                        print("element repeats in",i+1,"th column and in ",j+1,"th row according to laws of rows")
                else:
                        pos=d[a[j][i]]
                        print("element repeats in",int(pos/10)+1,"th column and in ",int(pos%10)+1,"th row according to laws of rows")
    if q==0:
      print("\n\n\n\n\t\t\t\tsuccess  👏👏👏👏  🎉🎉🎉\n\n\n\n\n\n")

def sucheck():
    print("Enter the sudoku")
    c=()
    for i in range(9):
        l=tuple(map(int,input().split()))
        c+=(l,)
    p=()
    print("enter the position of sure elements(Eg:12 for (1,2)\n 🔴enter 1 if you are playing sudoku game")
    if int(input())==1:
    	p=(13,16,17,22,25,29,34,37,39,48,51,53,54,56,58,59,61,72,74,76,81,85,89,91,94,97)   
    else:
    	p=tuple(map(int,input("enter the position").split()))
    os.system('clear')
    chcol(c,p)

#___________________________________________________________printing______________________________________________________________
def ques():
	print("Welcome to sudoku world")
	print("",end=" ")
	l=[[8,"_",7,1,5,4,3,9,6],["_",6,5,"_",2,7,"_",4,8],[3,"_",1,6,8,"_",7,5,2],[5,"_",3,"_",6,"_",2,7,"_"],[4,"_",2,5,"_",3,"_",8,9],[6,1,"_",9,7,2,4,3,"_"],["_",8,6,2,"_",5,"_",1,4],[1,5,4,"_",9,6,"_",2,3],[2,3,"_",8,"_",1,5,"_",7]]
	print("\n:---------------------:\n ")
	for i in range(9): 
		for j in range(9): 
			print (l[i][j],end=" ") 
			if (j+1)%3==0:
				print(":",end="")
		if (i+1)%3==0:
				print("\n:--------------------:",end="")
		
		
		print ('\n',end=" ") 
	print("\n\n\ninput answer")
	sucheck()
 	
	
while(1):
	print("________________sudoku________________")
	print("1.play sudoku\n2.checking sudoku\n3.solve sudoku \n4.help\n5.exit")
	c=int(input())
	if c==3:
		solve()   
	elif c==2:
		sucheck()
	elif c==1:
		ques()
	elif c==4:
		print("The classic Sudoku game involves a grid of 81 squares. The grid is divided into nine blocks, each containing nine squares. The rules of the game are simple: each of the nine blocks has to contain all the numbers 1-9 within its squares. Each number can only appear once in a row, column or box.")	
	elif c==5:
		print("thankyou for using sudoku game\n plz.. visit again😊")
		break	
	else:
		print("Incorrect statements")
		break