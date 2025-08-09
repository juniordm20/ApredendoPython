#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todos as informações possiveis sobre ela.
N = input("Digite algo: ")

print("Tipo primitivo:", type(N))
print("Só tem números? ", N.isnumeric())
print("Só tem letras? ", N.isalpha())
print("É alfanumérico? ", N.isalnum())
print("Está em maiúsculas? ", N.isupper())
print("Está em minúsculas? ", N.islower())
print("Está capitalizado? ", N.istitle())
