#-*- coding: utf8 -*-
#convertendo de real para inteiro
print 'int(3.14) =', int(3.14)

#convertendo de inteiro para real
print 'float(5) =', float(5)

#cálculo entre inteiro e real resulta em real
print "5.0/2+3=", 5.0/2+3

#inteiros em outra base
print "int('20', 8)",int('20', 8)#base 8
print "int('20', 16)", int('20', 16)#base 16

#operações com número complexos
c=3+4j
print 'c=', c
print 'parte real', c.real
print 'parte imaginária', c.imag
print 'conjugado', c.conjugate()

