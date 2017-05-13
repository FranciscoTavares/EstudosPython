#-*- coding:utf8 -*-

musicos=[('page','guitarrista','led zeppelin'),('fripp', 'guitarrista', 'king crimson')]

#parêmetros identificados pela ordem
mensagem = '{0} é {1} do {2}'

for nome,funcao, banda in musicos:
   print(mensagem.format(nome, funcao, banda))

mensagem = '{saudacao}, são {hora:02d}:{minutos:02d}'

print mensagem.format(saudacao='Bom dia',hora=8, minutos=23)

#Fatiar a string

#Para mostrar a string invertida basta colocar o terceiro parâmentro intervalo com -1
p='Python'
print p[::-1]

#para mostrar apenas a sílaba Py
print p[:2]

#para mostrar apenas a sílaba thon
print p [2:]

