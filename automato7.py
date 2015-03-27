#!/usr/bin/env python
# -*- coding: utf-8 -*-
print"================================================================================"

seq = raw_input ("Digite uma sequencia de 0 e 1:")
print "Sequencia Digitada: [",seq,"]"
print len(seq)
def confere(seq):
	soma = 0
	for i in range(len(seq)): 
		if (seq[i] == "1"):
			soma = soma + 1				
	return soma

resultado = confere(seq)
if((resultado % 5) == 0):
	print "VÁLIDO! O conjunto contém um número de Uns divisível por 5!"
else:
	print"INVÁLIDO! O conjunto não contém um número de Uns divisível por 5!"

print"================================================================================"