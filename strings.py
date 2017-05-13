#-*- coding:utf8 -*-
# operador '%' é usado para fazer interpolação de strings. A interpolação é mais eficiente no uso de memória do que a concatenação convencinal.

#símbolos usados na interpolação:
# %s = string
# %d = inteiro
# %o = octal
# %x = hexadecimal 
# %f = real
# %e = real exponencial
# %% = sinal de percentagem

#exemplos

s= 'kamila '
#concatenação
print 'The ' + s + 'run away'

#interpolação
print 'tamanho de %s => %d' %(s, len(s)-1)

#string tratada como sequência
for ch in s:
   if(ch != ' '):
       print ch

#strings são objetos
if s.startswith('k'): print s.upper()

#o que acontecerá?
print 3*s
# 3*s é consistente com s + s + s

#zeros a esquerda
print 'agora são %02d:%02d' %(16,30)

#real (número após o ponto controla as casas decimais)
print'percentagem: %.1f%%, exponencial:%.2e' %(5.333, 0.00314)

#octal e hexadecimal
print 'Decimal: %d, Octal: %o, Hexadecimal: %x' %(10, 10, 10)



