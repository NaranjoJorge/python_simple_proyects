#Count # of " " in string.

def run(x):
	spaces = [i for i in x if i == ' ']
	print(len(spaces))

if __name__ == '__main__':
	run('The birds ate butterflies while sleeping outside.')