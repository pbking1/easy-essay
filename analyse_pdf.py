from textblob import TextBlob
import re
import os, sys

text_list = []
text_all_str = ""
keyword_list = []
knowledge_base_pattern = []

# load the article
f = open("test_document")
for i in f.readlines():
	# load the keyword list
	if "Keyword" in i:
		i = i.replace(" ", "").lower()
		keyword_list = i.strip("\n").split(":")[1].split(",")
		continue
	# delete the data after the References
	if i == "References\n":
		break
	# delete the empty line
	if i not in ['\n', '\r\n']:
		text_list.append(i.lower().strip("\n"))
		text_all_str += (i.strip("\n") + " ")
f.close()

# first calculate the appearance of all the words in the document
token_list = text_all_str.replace(".", " ").replace(",", " ").split(" ")
all_str = TextBlob(text_all_str)

token_appearance = {}
for i in token_list:
	if i not in token_appearance and i != '':
		token_appearance[i] = token_list.count(i)

# sort the dictionary
import operator
sorted_token_appearance = sorted(token_appearance.items(), key=operator.itemgetter(1))
important_key_word = []
stop_word_list = []
f1 = open("stop_word.txt")
lines = f1.readlines()
for ind in lines:
	stop_word_list.append(ind.lower().strip("\n"))
f1.close()

for i in sorted_token_appearance:
	# the string is alpha and appear more than one times
	if i[1] > 1 and len(i[0]) >= 6 and i[0].isalpha() == True and i[0] not in stop_word_list:
		important_key_word.append(i[0])

# cut those lines that contain important keywords out
important_line_list = []
for line in text_list:
	for keyword in important_key_word:
		# if the line contain the key word
		# if the line has more than 5 letters
		if keyword in line and len(line.split(" ")) >= 6:
			# the sentence does not contain number
			if bool(re.search(r'\d', line)) == False:
				important_line_list.append(line)
				break

# iterate all the important line and analyze them using textblob
f3 = open("result", "a")
for index in range(0, len(important_line_list)):
	new_line_list = []
	#print index
	try:
		line_tag = TextBlob(important_line_list[index]).tags
		
		#combine the token into sentence again
		for token in line_tag:
			if "NN" in token[1] and len(token[0]) > 6:
				new_line_list.append(token[0] + " "),
		print new_line_list
		#f3.write(new_line_list)
	except:
		continue
	#print "\n"

f3.close()








