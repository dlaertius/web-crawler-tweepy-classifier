# -*- coding: utf-8 -*-
'''
@info Script criado para padronizar a quantidade de palavras em cada database.
@date Nov, 2 - 2016
@name Diogenes L.

'''

import random

files = ["FINAL_Negocios.txt","FINAL_Esportes.txt","FINAL_Entretenimento.txt"]

#4993 = [0]
#8843 = [1]
#7775 = [2]

for s in range(0,3):

	arq = open(files[s]).read().split()
	ct = 0
	list_x = []

	for w in arq:
		list_x.append(w)
		#print (s)
		ct+= 1

	total_base = 4993
	lita_size = len(list_x) - 1
	final_list = []

	data = range(total_base)
	unique_numbers = random.sample(range(1, lita_size), 4991)
	#print (unique_numbers)

	ct_unique = 4990

	while total_base:
		index = unique_numbers[ct_unique]
		final_list.append(list_x[index])
		total_base -= 1
		ct_unique -= 1

	print (len(final_list))
	#print (ct)

	f = open('x' + files[s],'w')
	string = ""
	for z in final_list:
		string += z + " "
	f.write(string)
