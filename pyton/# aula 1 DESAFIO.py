# aula 1 DESAFIO 

# nome = input('Qual é o seu nome?')
# print('prazer', nome , 'em te conhecer')

# desafio 2 

# nome = input('qual dia vc nasceu: ')
# mes = input('qual mes vc nasxceu: ')
# ano = input('qual ano vc nasceu: ')
# voce = nome, mes, ano 
# print(voce)

#desafio 3
# var1 = 10
# var2 = 2
# soma = var1 + var2
# print('soma igua á:', soma)

# n1 = int(input('digite um valor: '))
# n2 = int(input('digite outro valor:' ))
# s = n1 + n2
# print(s)

# desafio 4 

# a = input('digite algo: ')
# print(' o tipo primitivo desse valoe é :', type(a) )
# print('so tem espaços', a.isspace())
# print('é um numero:', a.isnumeric())
# print('é alfabetico,', a.isalpha())

# desafio 5

# n = int(input('digite um numero: '))
# a = n - 1
# s = n + 1
# print('analizando o valor {}, seu antecessor é {} e o sucessor é {}' .format(n,a,s))
# # ou pode ser assim tambem 1
# n= int(input('digite um numero:'))
# print('analizandoo valor {}, seu antecessor é {} e o seu sucessor é {}' . format(n, (n-1), (n+1)))


# # desafio 6
# numero = int(input(' Digite um numero: '))
# d = numero * 2 
# t = numero * 3
# raiz = numero **(1/2)
# print(' o dobre de {} é {} \n e o triplo é {} \n sua raiz é {:.2f},' .format(numero, d, t, raiz))

#ou pode ser 

# numero = int(input(' Digite um numero: '))
# print( 'o dobre de {} é {} \n e o triplo é {} \n sua raiz é {:.2f},' .format(numero, (numero*2), (numero*3), (numero**(1/2))))

# desafio sete , oito 

# nt1 = float(input(' digite sua 1° nota: '))
# nt2 = float(input('Digite sua segunda nota: '))
# media = (nt1 + nt2) / 2
# cent = float(media * 100)
# mil = float(media * 1000)
# print('nota 1 é  {} + nota2  {} tem a media de {} convertido para cent é = {:.0f} e em milimetros é {:.0f}' .format(nt1, nt2, media, cent, mil ))

# #ou pode ser assim, 

# print('nota 1 é  {} + nota2  {} tem a media de {} convertido para cent é = {} e em milimetros é {}' .format(nt1, nt2 , ((nt1+nt2)/2), (((nt1+nt2)/2) * 100 ), ((nt1+nt2)/2) * 1000 ))

# # desafio 9
# nm = int(input(' digite um numero: '))
# tab = nm*1 , nm*2 , nm*3, nm*4, nm*5
# print(tab)

#tabuada 
# num = int(input('digite  um numero para ver sua tabuada: ' ))
# print('-' * 12 )
# print(' {} * {} = {}' .format(num, 1, num*1))
# print(' {} * {} = {}' .format(num, 2, num*2))
# print(' {} * {} = {}' .format(num, 3, num*3))
# print(' {} * {} = {}' .format(num, 4, num*4)) 
# print('-' * 12)



#desafio 10 
# real = float(input(' quanto dinheiro vc tem na carteira?: '))
# dolar = real / 3.27
# print(' com r$ {} vc pode comprar {:.2f} US$' .format(real, dolar))


# #desafio 11
# alt = 10
# larg = 2
# area = alt * larg
# tinta = 2 * 20
# print(tinta)

# larg = float(input(' qual a da largura da parede: '))
# alt = float(input(' qual a da altura da parede: '))
# area = larg * alt
# print( ' Sua pareder tem a dimensao de {} x {} e sua area total é de {}' .format(larg, alt, area))
# tinta = area / 2 
# print('Para pintar essa area vc preceisarqa de {} lt de tinta ' .format(tinta))

# desafio 13
# sal = float(input('digite seu salario R$: '))
# aum =  (sal * 15 / 100)
# novo = sal + aum
# print( 'seu salario era R$ {} vc teve 15% de aumento que foi R${} agora seu novo salario é R${}' .format(sal, aum, novo))

#desafio 14 

# # desafio 15 
# dias = float(input(' quantos dias alugados:'))
# km = float(input('quantos km percorrido?: '))
# pagar = (dias * 60) + (km + 0.15)
# print('o total a pagar é {}' .format(pagar))

# aula 8  import
# import math
# num = int(input(' digite um numero :'))
# raiz = math.sqrt(num)
# print('a raiz quadrade de {} é exatamente {:.2f}' .format(num, raiz) )

# desafio 16 
# desafio 17
# desafio 18 

# desafio 19   SORTEAR UM ENTRE QUATROS ALUNOS

# import random
# n1 = str(input('primeiro aluno: '))
# n2 = str(input('segundo aluno: '))
# n3 = str(input(' terceiro aluno: '))
# n4 = str(input('quarto aluno: '))
# lista = (n1, n2, n3, n4 )
# escolhido = random.choice(lista)
# print(' O aluno escolhido foi {}' . format(escolhido))

# # desafio 20   MOSTRAR EMBARALHADO OS NOMES 
# import random
# n1 = str(input('primeiro aluno: '))
# n2 = str(input('segundo aluno: '))
# n3 = str(input(' terceiro aluno: '))
# n4 = str(input('quarto aluno: '))
# lista = [n1, n2, n3, n4 ]
# random.shuffle(lista)
# print(' a ordem da apresentação sera ')
# print(lista)


help()