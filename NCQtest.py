
################## task 1 ########################

import random
import numpy as np
def solution(n,list)
	rsult =np.zeros((5), dtype=int)
	x=0
	for i in list :
		if (i <= n) and (i >= 1) :
			rsult[x]+=1
		elif (i == (n+1)) :
			rsult=np.full(n , np.max(rsult))
		x+=1
	return(rsult)

N= random.randint(1 , 100000)
A=[]
for i in range(N) :
	A.append(random.randint(1 , N + 1))
print( solution(N,A))

######################## task 2 #####################

# at first I thought about solving this problem using binary tree  than I realized that recursivity work too because  we just have to  count the number of leaf within a binary tree we don't need to show  the pattern behind that result  def nbr_ways(n): 
def leaf_nbr(n)
    if n <= 1: 
        return n 
    return leaf_nbr(n-1) + leaf_nbr(n-2)



def solution(A, B):
	list=[]
	for i in range (len(A)):
		list.append(leaf_nbr( A[i] % ( 2 * B[i] ) ) + 1)
	return list

A=[]
B=[]

L= random.randint(1 , 50000)
for i in range(L):
	A.append(random.randint(1 , L))
	B.append(random.randint(1 , 30))
solution(A , B)


####################### task 3 #################

def val(A,S):
	return(abs(np.sum(np.multiply(A,S))))

# I used the same strategy as before where I just  searched for the minimum value without returning the sequence that laid to the resultdef  solution(A):

	return( min ( find_Min_Valu( A[ 1 : ] + A[1] ) , find_Min_Valu(A[ 1 : ] - A[1] )))

N= random.randint(1 , 20000)
for i in range(L):
	A.append(random.randint(-100 , 100))
solution(A)


#if we need to show pattern we  can use binary trees for task 2 and 3  

