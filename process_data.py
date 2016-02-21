import os, re

result_dict = {}
f = open("data/result.txt")
for i in f.readlines():
	temp = i.split(",")
	result_dict[temp[0]] = []
	for i in range(1, len(temp)):
		result_dict[temp[0]].append(temp[i])
print result_dict	

f.close()

# convert data
for key, val in result_dict.iteritems():
	#print str(key) + " " + str(val)
	for item in val:
		print "{source: \"" + key + "\", target: \"" + item.strip("\n") + "\", type:\"suit\"},"
