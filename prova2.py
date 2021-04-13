#inicio
def exercicio1():
  print('Coloque três notas: ')
  nota_1 = float(input())
  nota_2 = float(input())
  nota_3 =  float(input())
  return (f'Media do aluno é: {(nota_1 + nota_2 + nota_3) / 3}')
#fim
          
#inicio
def exercio2():
  num_elementos = int(input('Coloque tamanho da lista: '))
  lista = []
  for num in range (num_elementos):
    lista.append(input())
return lista
#fim

#inicio
def exercio3():
  opcao = input('Digite sua opção: ') 
  while opcao != 'z':
    if opcao == 'z':
      break
  elif opcao == 'a':
    print('Globo')
  else:
    print('SBT')
 #fim

#inicio
def professores(media):
  media_menor_7 = 0
porcentagem = len(medias) * 0.25
for media in media:
  if media < 7:
    media_menor_7 += 1
if media_menor_7 < porcentagem:
  return "Professor Coxa"
else:
  return "Professor Padrão"

professores([3, 8, 5, 9,3])
#fim
