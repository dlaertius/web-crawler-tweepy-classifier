# -*- coding: utf-8 -*-

from normalizr import Normalizr

arq = open("negocios.txt",'r')

arq_2 = open("FINAL_Negocios.txt",'w')

#arq_2 = open("FINAL_Negocios.txt", 'w')

normalizr = Normalizr(language='en')

texto = ""

for s in arq:
	 s = s.replace("\n", " ")
	 s = s.replace("?", " ")
	 s = s.replace('“', "")
	 s = s.replace(":", " ")
	 #s = s.replace("'", " ")
	 s = s.replace("+", " ")
	 s = s.replace(";", " ")
	 s = s.replace(",", " ")
	 s = s.replace('"', " ")
	 s = s.replace('(', " ")
	 s = s.replace(')', " ")
	 s = s.replace("\t", "")
	 s = s.replace('\\', "")
	 s = s.replace('‘', " ")
	 s = s.replace('!', " ")
	 s = s.replace('.', " ")
	 s = s.replace('”', " ")
	 s = s.replace('—', " ")
	 s = s.replace('–', " ")
	 s = s.replace('|', " ")
	 s = s.replace('’', " ")
	 s = s.replace('1', "")
	 s = s.replace('2', "")
	 s = s.replace('3', "")
	 s = s.replace('4', "")
	 s = s.replace('5', "")
	 s = s.replace('6', "")
	 s = s.replace('7', "")
	 s = s.replace('8', "")
	 s = s.replace('9', "")
	 s = s.replace('0', "")
	 s = s.replace('»', '')
	 s = s.replace('$', '')
	 s = s.replace('›', '')
	 #print (s)
	 texto = texto + s

texto = texto.lower()


normalizations = [
	('replace_urls', {'replacement': ' '}),
	('replace_punctuation', {'replacement': ' '}),
	('replace_emojis', {'replacement': ' '}),
	('replace_hyphens', {'replacement': ' '}),
	('replace_symbols', {'replacement': ' '}),
	'remove_accent_marks',
	'remove_stop_words',
	'remove_extra_whitespaces',
	]

arq_2.write(normalizr.normalize(texto, normalizations))

arq_2.close()
arq.close()

#calculando a quantidade total de palavras válidas porém repetidas da base. TOTAL : 4650
'''
arq_2 = open("FINAL_Entretenimento.txt", 'w')

st = ""
for z in arq_2:
	st += z

z = z.split()
print (z)
print (len(z))

arq_2.close()

'''
#print(normalizr.normalize(texto, normalizations))