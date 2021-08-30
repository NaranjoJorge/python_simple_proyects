#Programs that tells whether a word is a palindrome

word = input('Enter a word: ').lower().replace(' ', '')
if word == word[::-1]:
	print(word.capitalize() + ' is a palindrome')
else:
	print(word.capitalize() + ' is not a palindrome')
