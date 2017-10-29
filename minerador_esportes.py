# -*- coding: utf-8 -*-

import urllib
import json

list_cubs = ["cubs", "go cubs", "world series", "chicago", "wrigley", "GoCubsGo", "WorldSeries", "Wrigleyville"]
list_daughter = ["hotshot", "daughter", "abby hornacek" ,  "hot", "beatiful" ,"jeff hornacek" ,  "nba" ,  "new york knicks" ,  "usc trojans", "basketball"]
list_giants = ["giants", "good vibes", "dreamchasers", "metLife stadium", "dennis byrd" , "eli manning" , "justin pugh", "new york giants" , "odell beckham jr.", "nfl"]

#Giants cubs
dic_cubs = {}
dic_cubs["pos"] = 0
dic_cubs["neg"] = 0
dic_cubs["neutral"] = 0

#Giants daughter
dic_daug = {}
dic_daug["pos"] = 0
dic_daug["neg"] = 0
dic_daug["neutral"] = 0

#Giants dic
dic_giants = {}
dic_giants["pos"] = 0
dic_giants["neg"] = 0
dic_giants["neutral"] = 0



def sentiment_ana(phrase):
	params = {}
	params["text"] = phrase
	params = urllib.urlencode(params)
	sentiment = urllib.urlopen("http://text-processing.com/api/sentiment/", params)
	dec = json.loads(sentiment.read())
	return dec

def start():

	tweets_giants = 0
	tweets_cubs = 0
	tweets_daug = 0

	#Variáveis de controle para poder saber quantas palavras parecidas na frase tem.
	qt_cubs = 0
	qt_giants = 0
	qt_daugther = 0

	try:
		data_esportes = open("tweets_classificados/esportes/data.txt",'r')

	except:
		print ("Não foi possível recuperar o arquivo: 'tweets_classificados/esportes/data.txt'")

	for phrase in data_esportes:

		#Conta quantas palavras combinando com cada lista de palavras chave tem.
		#A que tiver mais palavras chaves combinando (qt..) será a rotulação para notícia.
		#Se possui ao menos duas palavras pois "A filha do técnico... "
		for cb in list_cubs:
			if cb in phrase:
				#print (cb)
				#print ("Cubs")
				qt_cubs += 1

		for cb in list_daughter:
			if cb in phrase:
				#print (cb)
				#print ("Daugther")
				qt_daugther += 1

		for cb in list_giants:
			if cb in phrase:
				#print (cb)
				#print ("Daugther")
				qt_giants += 1

		if(qt_cubs >= qt_giants and qt_cubs >= 2):

			if(qt_cubs >= qt_daugther):
				f = sentiment_ana(phrase).get('label')
				dic_cubs[str(f)] += 1
				tweets_cubs += 1
				print(phrase)

			#cubs menor que daugther.
			else:
				f = sentiment_ana(phrase).get('label')
				dic_daug[str(f)] += 1
				tweets_daug += 1
				print(phrase)

		elif(qt_daugther >= qt_giants and qt_daugther >= 2):

			if(qt_daugther >= qt_cubs):
				f = sentiment_ana(phrase).get('label')
				dic_daug[str(f)] += 1
				tweets_daug += 1
				print(phrase)

			#daugther menor que cubs
			else:
				f = sentiment_ana(phrase).get('label')
				dic_cubs[str(f)] += 1
				tweets_cubs += 1
				print(phrase)

		elif(qt_giants >= qt_cubs and qt_giants >= 2):

			if(qt_giants >= qt_daugther):
				f = sentiment_ana(phrase).get('label')
				dic_giants[str(f)] += 1
				tweets_giants += 1
				print(phrase)

			#giants menor que daughter.
			else:
				f = sentiment_ana(phrase).get('label')
				dic_daug[str(f)] += 1
				tweets_daug += 1
				print(phrase)

		qt_cubs = 0
		qt_giants = 0
		qt_daugther = 0

	print (dic_cubs)
	print (dic_daug)
	print (dic_giants)
	print("Qt Cubs: " + str(tweets_cubs) + " Qt Daughter: " + str(tweets_daug) + " Qt Giants: " + str(tweets_giants))

start()