# -*- coding: utf-8 -*-
import json
import re
import antispammer
import tweet_normalisation
import naivebayesclassifer
from normalizr import Normalizr


#Caminho/nome do arquivo que contém os tweets.
path = "python.json"

#Abri o arquivo e executa o spammer.
antispammer.start(path)

#Abre o arquivo sem spam para normalizar os tweets e classificar.
file = open("dataset.json", 'r')

data = open(r"palavra.txt",'w')

qt_esporte = 0
qt_negocios = 0
qt_entre = 0

data_esportes = open("tweets_classificados/esportes/data.txt",'w')
data_negocios = open("tweets_classificados/negocios/data.txt",'w')
data_entretenimento = open("tweets_classificados/entrete/data.txt",'w')

for line in file:
		
		dec = json.loads(line)

		try:
			tweet_text = dec['text'].lower()
			#print (tweet_text)
			#Tratar RT.

		except:
			print ("Não conseguiu recuperar o texto.")
			break
		
		tweet_normalizado = tweet_normalisation.normalisation(tweet_text)

		#Utilizado para limpar o que tiver no arquivo e escrever novamente.
		data.seek(0)
		data.truncate()
		data.write(tweet_normalizado)
		
		#Classifica o tweet, printa na tela e salva na variável que será usada para comparar a classe do tweet.
		classificação = naivebayesclassifer.tc.classify("palavra.txt")

		if (classificação == "esportes"): 
			data_esportes.write(tweet_normalizado + "\n")
			qt_esporte+= 1

		elif (classificação == "negocios"):
			data_negocios.write(tweet_normalizado + "\n")
			qt_entre += 1
		else:
			data_entretenimento.write(tweet_normalizado + "\n")
			qt_entre+= 1

		#print ("Classificação foi: " + str(classificação))
		
		#print (tweet_normalizado)

data_entretenimento.close()
data_negocios.close()
data_negocios.close()

#Após finalizar a classificação, será buscado tweets de 3 tópicos específicos e irá ser extraído
#a polaridade de cada notícia.

#minerador_esportes.start()
#minerador_negocios.start()

'''
data_negocios = open("tweets_classificados/negocios/data.txt",'r')
data_entretenimento = open("tweets_classificados/entrete/data.txt",'r')

'''



