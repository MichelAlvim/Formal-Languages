#!/usr/bin/env python
# -*- coding: utf-8 -*-
print"================================================================================"
seq = raw_input ("Digite uma sequencia de 0 e 1:")


print "Sequencia Digitada: [",seq,"]"
qnt = 0 
estado =0
for i in range(len(seq)):
	if (seq[i]== "0"):
		estado=1
		if(i != (len(seq))-1): 
			estado=2
			if(seq[i+1] == "0"):
				if(i+1 != (len(seq))-1):
					if(seq[i+2] == "0"):
						estado = 3
						qnt = qnt +1





if(qnt != 0):
	print "VÁLIDO!"                                                                                                                  
else:
	print"INVÁLIDO!"

print"================================================================================"