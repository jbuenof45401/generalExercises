pizza = ["tomate","queso","peperoni","jamon","masa"]
pizza_carnes = ['jamon','salchicha','salami']
pizza_pollo = ['pollo','tocineta','champiñones']

pizza_especial = pizza_carnes+pizza_pollo

print(pizza_especial)

print(pizza)

print('El cuarto elemento es ', pizza[3])

print('Mi tajada de pizza tiene ', pizza[1:3])

print('Mi tajada de pizza tiene ', pizza[2:])

print('mi tajada de pizza tiene ', pizza[:3])
# posiciones del arreglo en forma inversa
print('El ultimo elemento de mi pizza es ', pizza[-1])

print('El ultimo elemento de mi pizza es ', pizza[-3:-1])

pizza[-1]='piña'
print(pizza)

pizza_ultra_mega_carnes = pizza_carnes * 20
pizza_especial_extra_pollo = (pizza_pollo*2)+pizza_carnes
print(pizza_especial_extra_pollo)

print('la pizza especial tiene mani?', 'mani' in pizza_especial)

pizza_pollo.append("Ciruela")
print(pizza_pollo)

pizza_pollo.insert(0,'queso')
print(pizza_pollo)

ciruela = pizza_pollo.pop()
print(pizza_pollo , ciruela)

pizza_ultra_mega_carnes.remove('jamon')
print(pizza_ultra_mega_carnes)


#pizza_pollo.sort()
print(pizza_pollo)


pizza_ordenada = sorted(pizza_pollo)

print(pizza_ordenada)