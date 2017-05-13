#-*- coding:utf8 -*-

#módulo string
import string

#cria uma strng template
st = string.Template('$aviso aconteceu em $quando')

print st.substitute({'aviso':'Falta de eletrecidade', 'quando':'31 de março de 2012'})
