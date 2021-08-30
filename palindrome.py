#Programs that tells whether a word is a palindrome

word = input('Enter a word: ')
modify_word = word.lower().replace(' ', '')
if modify_word == modify_word[::-1]:
	print(word + ' is a palindrome')
else:
	print(word + ' is not a palindrome')
