#Converts CAD, BRL & CDF to USD.

menu = '''
Welcome to the money exchange

1- Canadian dollar
2- Brazilian real
3- Congolese franc
'''
print(menu)
currency = int(input('Please select the number according to your currency: '))
amount = float(input('Please select the amount you wish to exchange: '))
dollars = 0
if currency == 1:
	dollars = amount * 0.79
elif currency == 2:
	dollars = amount * 0.19
elif currency == 3:
	dollars = amount * 0.00050
else:
	print('You did not select a number between 1 and 3.')
print(round(dollars, 3))
