# -*- coding: utf-8 -*-

import urllib
import json

list_airbnb = ["airbnb", "andrew cuomo" , "bernie sanders", "opinion", "politics", "real estate","midtown", "boerumhill", "carroll gardens", "cobble hill", "gowanus", "park slope", "boroughs", "food", "brooklyn", "the insider blog"]
list_brexit = ["brexit", "britain", "European Union" ,  "eu", "london" ,"adam durant", "thrives", "future trading"]
list_ibm = ["ibm", "watson", "paying", "big money", "A.I." , "technology" , "tom austin", "applied-science" , "projects", "frank gens", "bet", "executives", "moneymaking"]

#Giants cubs
dic_airbnb = {}
dic_airbnb["pos"] = 0
dic_airbnb["neg"] = 0
dic_airbnb["neutral"] = 0

#Giants daughter
dic_brexit = {}
dic_brexit["pos"] = 0
dic_brexit["neg"] = 0
dic_brexit["neutral"] = 0

#Giants dic
dic_ibm = {}
dic_ibm["pos"] = 0
dic_ibm["neg"] = 0
dic_ibm["neutral"] = 0



def sentiment_ana(phrase):
	params = {}
	params["text"] = phrase
	params = urllib.urlencode(params)
	sentiment = urllib.urlopen("http://text-processing.com/api/sentiment/", params)
	dec = json.loads(sentiment.read())
	return dec

def start():

	tweets_ibm = 0
	tweets_airbnb = 0
	tweets_brexit = 0

	#Variáveis de controle para poder saber quantas palavras parecidas na frase tem.
	qt_airbnb = 0
	qt_brexit = 0
	qt_ibm = 0

	try:
		data_esportes = open("tweets_classificados/negocios/data.txt",'r')

	except:
		print ("Não foi possível recuperar o arquivo: 'tweets_classificados/negocios/data.txt'")

	for phrase in data_esportes:

		#Conta quantas palavras combinando com cada lista de palavras chave tem.
		#A que tiver mais palavras chaves combinando (qt..) será a rotulação para notícia.
		#Se possui ao menos duas palavras pois "A filha do técnico... "
		for cb in list_airbnb:
			if cb in phrase:
				#print (cb)
				#print ("Cubs")
				qt_airbnb += 1

		for cb in list_brexit:
			if cb in phrase:
				#print (cb)
				#print ("Daugther")
				qt_ibm += 1

		for cb in list_ibm:
			if cb in phrase:
				#print (cb)
				#print ("Daugther")
				qt_brexit += 1

		if(qt_airbnb >= qt_brexit and qt_airbnb >= 2):

			if(qt_airbnb >= qt_ibm):
				f = sentiment_ana(phrase).get('label')
				dic_airbnb[str(f)] += 1
				tweets_airbnb += 1
				print(phrase)

			#cubs menor que daugther.
			else:
				f = sentiment_ana(phrase).get('label')
				dic_brexit[str(f)] += 1
				tweets_brexit += 1
				print(phrase)

		elif(qt_ibm >= qt_brexit and qt_ibm >= 2):

			if(qt_ibm >= qt_airbnb):
				f = sentiment_ana(phrase).get('label')
				dic_brexit[str(f)] += 1
				tweets_brexit += 1
				print(phrase)

			#daugther menor que cubs
			else:
				f = sentiment_ana(phrase).get('label')
				dic_airbnb[str(f)] += 1
				tweets_airbnb += 1
				print(phrase)

		elif(qt_brexit >= qt_airbnb and qt_brexit >= 2):

			if(qt_brexit >= qt_ibm):
				f = sentiment_ana(phrase).get('label')
				dic_ibm[str(f)] += 1
				tweets_ibm += 1
				print(phrase)

			#giants menor que daughter.
			else:
				f = sentiment_ana(phrase).get('label')
				dic_brexit[str(f)] += 1
				tweets_brexit += 1
				print(phrase)

		qt_airbnb = 0
		qt_brexit = 0
		qt_ibm = 0

	print (dic_airbnb)
	print (dic_brexit)
	print (dic_ibm)
	print("Qt Cubs: " + str(tweets_airbnb) + " Qt Daughter: " + str(tweets_brexit) + " Qt Giants: " + str(tweets_ibm))

start()