def negate(opnd):
	binary = '{:032b}'.format(int(opnd))
	binary_list = list(map(int,binary))
	binary_2s_compl = [0 for i in range(32)]
	flag = 0
	for i in range(31,-1,-1):
		if flag == 1:
			binary_2s_compl[i] = int(not(binary_list[i]))
		else:
			if int(binary[i]) == 1:
				flag += 1
			binary_2s_compl[i] = int(binary[i])

	binary_2s_compl = "".join(list(map(str,binary_2s_compl)))
	return binary_2s_compl