#!urs/bin/python
# -*- coding: utf-8 -*-

import json
import re

'''

1. Verificar se os tweets estão em inglês.
2. Verificar quantidade seguidores.
3. Verificar se tem link no twitter.
4. Verificar se o mesmo usuário já twitou.

'''

def add_id(id, ids):
	ids.append(id)
	ids.sort()

def spam_treatment(arq, arq_end, arq_spam, ids):

	link1 = "http://"
	link2 = "https://"
	link3 = "www."

	for line in arq:
		
		dec = json.loads(line)

		try:
			language = dec.get('user').get('lang')
			#print (language)
		except:
			print("Não conseguiu recuperar o idioma.")
			break

		try:
			followers_count = dec.get('user').get('followers_count')
			#print (followers_count)
		except:
			#print("Não conseguiu recuperar a quantidade de seguidores.")
			break

		try:
			tweet_text = dec['text'].lower()
			#print (tweet_text)
		except:
			print ("Não conseguiu recuperar o texto.")
			break

		try:			
			tweet_id = int(dec.get('user').get('id'))
			print (tweet_id)
		except:
			print ("Não conseguiu recuperar o id.")
			break

		if language == "en":
			#print ("Em inglês")

			if followers_count > 0:
				#print ("Seguidores > 0")


				if (tweet_text.startswith("RT")) != True and ("RT" in tweet_text) != True: 

					if link1 not in tweet_text and link2 not in tweet_text and link3 not in tweet_text:

						if tweet_id not in ids:

							add_id(tweet_id,ids)

							arq_end.write(line)

							print ("IDs: " + str(ids))

						else:
							print ("Já está na lista o id.")
					else:
							print("Contém Link.")
							arq_spam.write(line)
			else:
				print("Não tem nenhum seguidor.")
				arq_spam.write(line)
		else:
			print("Linguagem não está em inglês.")



def start(path):

	arq = open(str(path),'r')

	arq_end = open("dataset.json",'w')

	arq_spam = open("dataspam.json",'w')

	id = []

	#Tratando o spam.
	spam_treatment(arq,arq_end,arq_spam,id)
										
	arq.close()
	arq_end.close()
	arq_spam.close()

