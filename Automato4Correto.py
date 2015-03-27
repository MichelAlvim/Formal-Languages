#!/usr/bin/env python
# -*- coding: utf-8 -*-
print"================================================================================"
seq = raw_input ("Digite uma sequencia de 0 e 1:")


print "Sequencia Digitada: [",seq,"]"
qnt = 0 
estado =0

for i in range(len(seq)): 
	if (seq[i]== "0"):
		estado=2
		if(i != (len(seq))-1): 
			if(seq[i+1] == "0"):
				estado =3
			else:
				estado = 1
	elif (seq[i] == "1"):
		estado =1
		if(i != (len(seq))-1): 
			if(seq[i+1] == "1"):
				estado =3
			else:
				estado =2
if(estado == 3):
	print "VÁLIDO!"                                                                                                                  
else:
	print"INVÁLIDO!"

print"================================================================================"