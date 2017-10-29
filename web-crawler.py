#!/usr/bin/env python
# -*- coding: utf-8 -*-

#10105169@143.107.137.90

'''

Site com demais opções:
	http://www.guiademidia.com.br/jornaisdesaopaulo.htm

Primeira opção:
	http://www.gazetasp.com.br/
	http://www.diariosp.com.br/

Como funcionaria: 
	Este script iria recuperar as páginas html bem como 
	sua classificação quando a esportes, econômia, política
	e retornar para arquivos .txt ou .json diferentes.

Tutorial:
	http://stackoverflow.com/questions/328356/extracting-text-from-html-file-using-python

'''

import urllib
from bs4 import BeautifulSoup

esportes = ["http://www.nytimes.com/pages/sports", "http://www.nbcnewyork.com/news/sports/", 
"http://www.nydailynews.com/sports", "http://nypost.com/sports/"]

negocios = ["http://www.nytimes.com/pages/business/index.html"
				,"http://www.bizjournals.com/newyork/news/"
				,"http://www.nbcnewyork.com/news/business/"
				,"http://www.crainsnewyork.com/news"]

entretenimento = ["http://www.nydailynews.com/entertainment",
				"http://www.amny.com/entertainment",
				"http://www.nbcnewyork.com/entertainment/",
				"http://www.syracuse.com/entertainment/"]

url = entretenimento[3]
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

# kill all script and style elements
for script in soup(["script", "style"]):
    script.extract()    # rip it out

# get text
text = soup.get_text()

#print text

# break into lines and remove leading and trailing space on each
lines = (line.strip() for line in text.splitlines())
# break multi-headlines into a line each
chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
# drop blank lines
text = '\n'.join(chunk for chunk in chunks if chunk)

file = open("syracuse.xml",'w')
text = text.encode('utf-8')
file.write(text)
file.close()
