# -*- coding: utf-8 -*-

# Faça um programa que receba duas notas digitadas pelo usuário Se a nota for maior ou igual a seis, escreva aprovado, senão escreva reprovado




N1 = float(input("Digite a primeira nota"))
N2 = float(input("Digite a segunda nota"))

media = (N1 + N2) / 2

print("Sua nota final é:", media)
if media < 6.0:
    print("REPROVADO")

elif media >= 6.0:
    print("APROVADO")

