def matrix_dot_vector(a:list[list[int|float]],b:list[int|float])-> list[int|float]:
	dot = []
	if(len(b)==len(a[0])):
		for i in range(len(a)):
			x=0
			for j in range(len(a[0])):
				x=x+a[i][j]*b[j]
			dot.append(x)
		return dot
	else:
		return -1
