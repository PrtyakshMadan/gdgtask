def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	if(mode == 'row'):
		new = []
		for i in range(len(matrix)):
			sum = 0
			for j in range(len(matrix[0])):
				sum = sum+matrix[i][j]
			mean = sum/len(matrix[0])
			new.append(mean)
		return new
	elif(mode == 'column'):
		new1 = []
		sum =0
		for i in range(len(matrix[0])):
			sum=0
			for j in range(len(matrix)):
				sum = sum + matrix[j][i]
			mean2 = sum/len(matrix)
			new1.append(mean2)
			
		return new1
	else:
		return -1
