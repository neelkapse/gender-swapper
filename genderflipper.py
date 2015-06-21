import urllib, urllib2, Tkinter

gender_flip = {
	'he': 'she',
	'himself': 'herself',
	'widow': 'widower', 'widows': 'widowers',
	'actor': 'actress', 'actors': 'actresses',
	'male': 'female', 'males': 'females',
	'man': 'woman', 'men': 'women',
	'gentleman': 'lady', 'gentlemen': 'ladies',
	'boy': 'girl', 'boys': 'girls',
	'schoolgirl': 'schoolboy',
	'son': 'daughter', 'sons': 'daughters',
	'mother': 'father', 'mothers': 'fathers', 
	'brother': 'sister', 'brothers': 'sisters',
	'uncle': 'aunt', 'uncles': 'aunts',
	'nephew': 'neice', 'nephews': 'neices',
	'mother-in-law': 'father-in-law',
	'bachelor': 'spinster',
	'boyfriend': 'girlfriend',
	'emperor': 'empress',	
	'hero': 'heroine',	
	'host': 'hostess',	
	'landlord': 'landlady',	
	'steward': 'stewardess',
	'waiter': 'waitress',
	'fireman': 'firefighter',
	'policeman': 'policewoman',
	# Quite interesting! no female equivalent for mailman!
	'mailman': 'mailwoman', 
	'salesman':	'saleswoman',
	'blond': 'blonde',
	'masseur': 'masseuse',
	'bridegroom': 'bride',
	'duke': 'duchess',
	'earl': 'countess',
	'king': 'queen',
	'prince': 'princess',
	'princes': 'princesses',
	'master': 'mistress',
	'masters': 'mistresses',
	'headmaster': 'headmistress',
	'headmasters': 'headmistresses',
	'mr': 'ms',
	'sorcerer': 'sorceress'
}

punctuation = {
	'.', ',', '!', '?', ':', ';', '"', "'"
}

def flip_file(filename, names):
	f = open(filename, 'r')
	output_text = flip(f.read(), names)
	f = open("output.txt", 'w')
	f.write(output_text)
	return output_text

def flip(text, names):
	
	# A dictionary of indexes at which case needs to be switched, and the case 
	# to be switched to.
	# 1: Title , 2: UPPER
	case_switch_dict = {} 	

	input_list = text.split()

	new_input_list = []
	for s in input_list:
		new_input_list.append(s)
		new_input_list.append(' ')

	input_list = new_input_list 	

	k = len(input_list)
	i = 0
	while i < k: 			
		for c in punctuation:
			# ensure that the punctuation character is not checked for punctuation
			if len(input_list[i]) > 1: 						
				if input_list[i].startswith(c):
					input_list.insert(i, c)
					# increment i by only one so that the same word is checked again for the "' case
					i = i+1									
					input_list[i] = input_list[i][1:]
					k = k+1
				elif input_list[i].endswith(c):
					input_list.insert(i+1, c)
					input_list[i] = (input_list[i])[:-1]
					i = i-1
					k = k+1
		i = i+1

	for i in range(len(input_list)):
		s = input_list[i]
		if s.istitle():
			case_switch_dict[i] = 1
			# only switch words that are in one of the two cases; prevents 
			# "iPod" and similar from being changed. Assumes that no 
			# gender-specific word will have odd case structure.
			input_list[i] = s.lower() 		
		elif s.isupper():
			case_switch_dict[i] = 2
			input_list[i] = s.lower()

	output_list = []
	for i in range(len(input_list)):
		s = input_list[i]
		flip = False

		if s == "hers":
			output_list.append("his")
			flip = True
		elif s == "her":
			# if followed by NN, NNS, or RB), use "his"
			if (not input_list[i+2] == ' ') and part_of_speech(input_list[i+2]): 	
				output_list.append("his")
				flip = True
			# else use "him"
			else:									
				output_list.append("him")
				flip = True
		elif s == "him":
			output_list.append("her")
			flip = True
		elif s == "his":
			for c in punctuation:
				if input_list[i+1] == c:
					output_list.append("hers")
					flip = True
					break
			if not flip:
				output_list.append("her")
				flip = True	
		else:
			for male, female in gender_flip.items():
				if s == male:
					output_list.append(female)
					flip = True
				elif s == female:
					output_list.append(male)
					flip = True
		
		for male, female in names.items():
			if s == male:
				output_list.append(female)
				flip = True
			elif s == female:
				output_list.append(male)
				flip = True

		if not flip:
			output_list.append(s)

	assert len(input_list) == len(output_list)

	for i in range(len(output_list)):
		if (i in case_switch_dict) and (case_switch_dict[i] == 1):
			output_list[i] = output_list[i].title()
		elif (i in case_switch_dict) and (case_switch_dict[i] == 2):
			output_list[i] = output_list[i].upper()

	output_text = ''
	for s in output_list:
		output_text += s
	return output_text

def part_of_speech(word):
	url = 'http://text-processing.com/api/tag/'
	values = {'text' : word}

	data = urllib.urlencode(values)
	req = urllib2.Request(url, data)
	response = urllib2.urlopen(req)
	response_page = response.read()

	return response_page[-5:-3] == "NN" or response_page[-5:-3] == "RB" or response_page[-6:-3] == "NNS"
	