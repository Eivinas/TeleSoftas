def print_list(a_list):
	for i in range(0, len(a_list)):  # Lists elements starts from 0
		print('Element {} = {}'.format(str(i),str(a_list[i])))
a_list = [1, 2, 3, 5, 7, 9]
print_list(a_list)