def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
	transpose = []

	for i in range(len(a[0])):
		new = []
		for j in range(len(a)):
			new.append(a[j][i])
		transpose.append(new)
	return transpose

