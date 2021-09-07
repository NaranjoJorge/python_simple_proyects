#Program that gets index and values from list.

def run(lst):
	result = [(i, lst[i]) for i in range(0, len(lst))]
	print(result)

if __name__ == '__main__':
	run(['hi', 4, 8.99, 'apple', ('t,b','n')])