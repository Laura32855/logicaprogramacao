#inicio 
def atividade1():
  for c in range (0, 100):
  if c % 5 == 0:
    print(c, end=" ")
#fim

#inicio
def atividade2():
  n = int(input('Digite o tamanho da lista: '))
  lista = [0] * n
  print(lista)
#fim

#inicio
def atividade3():
  lista = [1, 10, 6, 8, 2]
  cont = 0
  for c in lista:
    if c > 5:
      cont += 1
      print(f'A quantidade de números maiores que "5" é: {cont}')
#fim

#inicio
def exercicio4():
  opcao = input()
  while opcao != 'd':
    if opcao == 'a':
      print('PSG')
    elif opcao == 'b':
      print('BAYER')
 #fim 
    
    
