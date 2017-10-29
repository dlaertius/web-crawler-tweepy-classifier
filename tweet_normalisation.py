# -*- coding: utf-8 -*-

import re
from normalizr import Normalizr
from spell import correction

def normalisation(tweet):
	mention_removed = re.sub(r'(?:@[\w_]+)', '', tweet.lower())
	html_removed = re.sub(r'<[^>]+>', '', mention_removed)
	hashtag_removed = re.sub(r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)", '', html_removed)
	removed_repeated_chars = re.sub(r'(.)\1+', r'\1\1', hashtag_removed)
	normalised_text1 = re.sub(' +',' ', removed_repeated_chars)
	
	normalizr = Normalizr(language='en')

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

	normalised_text2 = normalizr.normalize(normalised_text1, normalizations)
	array_words = normalised_text2.split()
	#print (array_words)

	normalised_text3 = [correction(word) for word in array_words]
	normalised_tweet = " ".join(normalised_text3)

	return normalised_tweet

print (normalisation("@george <br> this     á ? ! ---  $ http://google.com Epizode from #narcos was fucking amazin!"))