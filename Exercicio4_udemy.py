primeiro = int(input('Primeiro numero: '))

segundo = int(input('Segundo numero : '))

terceiro = int(input('Terceiro numero: '))

if(terceiro < segundo):

  aux = terceiro

terceiro = segundo

segundo = aux

if(segundo < primeiro):

 aux= segundo

segundo = primeiro

primeiro = aux

if(terceiro < segundo):

 aux= terceiro

terceiro = segundo

segundo = aux

print("Lista Ordenada")

print('Primeiro = ' ,primeiro)

print('Segundo = ' ,segundo)

print('Terceiro = ' ,terceiro)

