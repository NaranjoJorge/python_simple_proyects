def run():
	my_list = [1, 'hello', True, 4.5]
	my_dict = {
		'first_name': 'Michale',
		'last_name': 'Brit'
	}
	super_list = [
		{'first_name': 'Michale', 'last_name': 'Brit'},
		{'first_name': 'Hernando', 'last_name': 'Brit'},
		{'first_name': 'Oreste', 'last_name': 'Espitia'},
		{'first_name': 'Ignacio', 'last_name': 'Perez'},
	]

	super_dict = {
		'natural_numbers': [1, 2, 3, 4],
		'integer_numbers': [-1, -2, 0],
		'floating_numbers': [3.4, 4.5, 2.3]
	}

	for key, value in super_dict.items():
		print(key, '  ', value)

if __name__ == '__main__':
	run()
