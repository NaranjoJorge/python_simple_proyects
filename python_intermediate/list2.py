#List of all consonants in string

def run():
	string = 'we dance alone'
	consonants = [x for x in string if x not in 'a, e, i, o, u, " "']
	print(consonants)

if __name__ == '__main__':
	run()