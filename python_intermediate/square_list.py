def run ():
	square_list = []
	# i = 1
	# while i <= 100:
	# 	y = i ** 2
	# 	square_list.append(y)
	# 	i += 1
	square_list = [i**2 for i in range(1, 101) if i % 3 != 0]
	print(square_list)

if __name__ == '__main__':
	run()
