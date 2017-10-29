# -*- coding: utf-8 -*-

import urllib
import json

list_hp = ["magical","triwizard","Ithaca", "wizarding", "weekend", "guide to 4 days", "Harry Potter", "west green st.","celebration","festival day"]
list_trump = ["snl","Trump", "Alec Baldwin", "skits", "criticizes", "baldwin", "urges"]
list_wilde = ["babybumps","Olivia Wilde", "Jason Sudeikis","baby girl","hollywood", "couple", "second child"]

#Giants cubs
dic_hp = {}
dic_hp["pos"] = 0
dic_hp["neg"] = 0
dic_hp["neutral"] = 0

#Giants daughter
dic_trump = {}
dic_trump["pos"] = 0
dic_trump["neg"] = 0
dic_trump["neutral"] = 0

#Giants dic
dic_wilde = {}
dic_wilde["pos"] = 0
dic_wilde["neg"] = 0
dic_wilde["neutral"] = 0



def sentiment_ana(phrase):
	params = {}
	params["text"] = phrase
	params = urllib.urlencode(params)
	sentiment = urllib.urlopen("http://text-processing.com/api/sentiment/", params)
	dec = json.loads(sentiment.read())
	return dec

def start():

	tweets_wilde = 0
	tweets_hp = 0
	tweets_trump = 0

	#Variáveis de controle para poder saber quantas palavras parecidas na frase tem.
	qt_hp = 0
	qt_trump = 0
	qt_wilde = 0

	try:
		data = open("tweets_classificados/esportes/data.txt",'r')

	except:
		print ("Não foi possível recuperar o arquivo: 'tweets_classificados/esportes/data.txt'")

	for phrase in data:

		#Conta quantas palavras combinando com cada lista de palavras chave tem.
		#A que tiver mais palavras chaves combinando (qt..) será a rotulação para notícia.
		#Se possui ao menos duas palavras pois "A filha do técnico... "
		for cb in list_hp:
			if cb in phrase:
				#print (cb)
				#print ("Cubs")
				qt_hp += 1

		for cb in list_trump:
			if cb in phrase:
				#print (cb)
				#print ("Daugther")
				qt_wilde += 1

		for cb in list_wilde:
			if cb in phrase:
				#print (cb)
				#print ("Daugther")
				qt_trump += 1

		if(qt_hp >= qt_trump and qt_hp >= 2):

			if(qt_hp >= qt_wilde):
				f = sentiment_ana(phrase).get('label')
				dic_hp[str(f)] += 1
				tweets_hp += 1
				print(phrase)

			else:
				f = sentiment_ana(phrase).get('label')
				dic_trump[str(f)] += 1
				tweets_trump += 1
				print(phrase)

		elif(qt_wilde >= qt_trump and qt_wilde >= 2):

			if(qt_wilde >= qt_hp):
				f = sentiment_ana(phrase).get('label')
				dic_trump[str(f)] += 1
				tweets_trump += 1
				print(phrase)

			else:
				f = sentiment_ana(phrase).get('label')
				dic_hp[str(f)] += 1
				tweets_hp += 1
				print(phrase)

		elif(qt_trump >= qt_hp and qt_trump >= 2):

			if(qt_trump >= qt_wilde):
				f = sentiment_ana(phrase).get('label')
				dic_wilde[str(f)] += 1
				tweets_wilde += 1
				print(phrase)

			else:
				f = sentiment_ana(phrase).get('label')
				dic_trump[str(f)] += 1
				tweets_trump += 1
				print(phrase)

		qt_hp = 0
		qt_trump = 0
		qt_wilde = 0

	print ("Dic Hp: ")
	print (dic_hp)
	print ("======")
	print ("Dic Trump: ")
	print (dic_trump)
	print("=======")
	print ("Dic Wilde")
	print (dic_wilde)
	print("=======")
	print("Qt HP: " + str(tweets_hp) + " Qt Trump: " + str(tweets_trump) + " Qt Wilde: " + str(tweets_wilde))

start()