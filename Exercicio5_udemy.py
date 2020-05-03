# -*- coding: utf-8 -*-






n1 = float(input("Primeiro numero:"))

n2 = float(input("Segundo numero:"))




opc = input('Escolha qual operação vc deseja fazer + - * /    ')

if opc == "+":
   print(n1, " + ", n2, " = ",  n1 + n2)
elif opc == "-":
   print(n1, " - ", n2, " = ", n1 - n2)
elif opc == "*":
   print(n1, " * ", n2,  " = ", n1 * n2)
elif opc == "/":
   print(n1, " / ", n2, " = ", n1 / n2)
else:
   print("Operador não encontrado")








