pesos = input('Ingrese un valor en pesos: ')
pesos = float(pesos)
dolares = pesos / 3829
dolares = round(dolares, 3)
dolares = str(dolares)
print('Tienes $' + dolares + ' dolares.')