#List of numbers from 1 to 1000 that contain digit 3.

def run():
	three = [x for x in range(1, 1001) if '3' in str(x)]
	print(three)

if __name__ == '__main__':
	run()