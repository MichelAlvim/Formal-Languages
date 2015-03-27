#!/usr/bin/env python
# -*- coding: utf-8 -*-
print"================================================================================"
seq = raw_input ("Digite uma sequencia de 0 e 1:")

print "Sequencia Digitada: [",seq,"]"
print len(seq)
def confere(seq):
	for i in range(len(seq)): 
		if (seq[i]== "0"):
			if(i != (len(seq))-1): 
				if(seq[i+1] == "0"):
					return 1
		elif (seq[i] == "1"):
			if(i != (len(seq))-1): 
				if(seq[i+1] == "1"):
					return 1

	return 0

resultado = confere(seq)
if(resultado == 1):
	print "VÁLIDO! O conjunto contém a sequencia 00 ou 11!"
else:
	print"INVÁLIDO! O conjunto não contém a sequencia 00 ou 11!"
print"================================================================================"