import urllib.request 
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import csv
import nltk
from nltk.tag import pos_tag
import time
import os



'''
How the script works:
1) read saved html pages - pages should be save in numerical order > A for loop to read them 
2) Get all the attributs from all the HTML > append them into a common list
3) Sort in individual lists
4) Add trend name in the individual lists
5) Check for company names
6) check Geography
7) Export final List

'''
d = os.getcwd() 
print ("Current directory: ",d)
path =  "F:\\fintech 2016-march2017\insurtech17" # Set path of new directory here
os.chdir(path)
new_d = os.getcwd() 
print ("New directory: ",new_d)
dir_file_list = os.listdir(path)
print (len(dir_file_list))








# 1 Read saved HTML pages + Get all the attributs + Sort in individual lists

collabList = [ ]
expanList = [ ]
fintecList = [ ]
investList = [ ]
islambkList = [ ]
regulatList = [ ]

for s in dir_file_list:
	
	print (s)
	file = open(s, encoding="utf8")
	content = file.read()

	bsObj = BeautifulSoup(content, "html5lib")

	items  = bsObj.findAll("div",{"class":"_cnc"})

	for item in items:

		title = item.h3.text
		link = item.a['href']
		datez = item("span",{"class":"f nsa _uQb"})
		dateFinal = datez[0].text
		source = item("span",{"class":"_tQb _IId"})
		sourceFinal = source[0].text
		snippet = item("div",{"class":"st"})
		snippetFinal = snippet[0].text

		result = [title,snippetFinal,link,dateFinal,sourceFinal]
		# rowTitle = title+snippetFinal
		rowTitle = title


		if "tie-up" in rowTitle or "partner" in rowTitle or "collaborate" in rowTitle or "collaboration" in rowTitle or "partners" in rowTitle or "ties-up" in rowTitle or "mou" in rowTitle or "merge" in rowTitle or "ties up" in rowTitle:
			collabList.append(result)
		if "IPO" in rowTitle or "rebrand" in rowTitle or "opens" in rowTitle or "expand" in rowTitle or "open" in rowTitle or "grow" in rowTitle or "launch" in rowTitle or "to open" in rowTitle or "expansion" in rowTitle:
			expanList.append(result)
		if  "fintech" in rowTitle or "smartphone" in rowTitle or "tablet" in rowTitle or "online" in rowTitle or "digital" in rowTitle or "tech" in rowTitle or "technology" in rowTitle or "virtual" in rowTitle or "app" in rowTitle or "mobile" in rowTitle:
			fintecList.append(result)
		if "raise" in rowTitle or "stake" in rowTitle or "funding" in rowTitle or "sells" in rowTitle or "acquire" in rowTitle or "invest" in rowTitle or "raise" in rowTitle or "sell" in rowTitle or "raising" in rowTitle or "merge" in rowTitle:
			investList.append(result)
		if 	"islamic" in rowTitle or "sharia" in rowTitle or "shariah" in rowTitle or "shariat" in rowTitle:
			islambkList.append(result)
		if "probe" in rowTitle or "rule" in rowTitle or "licence" in rowTitle or "permit" in rowTitle or "basel" in rowTitle or "governance" in rowTitle or "IMF" in rowTitle or "bailout" in rowTitle or "regulator" in rowTitle or "government" in rowTitle or "federal" in rowTitle or "federal reserve" in rowTitle or "privatisation" in rowTitle or "privatization" in rowTitle or "bank of England" in rowTitle or "central bank" in rowTitle or "law" in rowTitle or "regualtion" in rowTitle:
			regulatList.append(result) 

	time.sleep(3)

print("Collaboration: ",len(collabList))
print("expansion: ",len(expanList))
print("fintech: ",len(fintecList))
print("investment: ",len(investList))
print("islamic insurance: ",len(islambkList))
print("regualtions: ", len(regulatList))

sumIndexed  = len(collabList)+len(expanList)+len(fintecList)+len(investList)+len(islambkList)+len(regulatList)

print("Total Indexed: ",sumIndexed)

# Adding trend name
# collabList2 = collabList
for cItem in collabList:
	cItem.append("Collaboration")

# expanList2 = [expanList]
for eItem in expanList:
	eItem.append("Expansion")

# fintecList2 = [fintecList]
for fItem in fintecList:
	fItem.append("Fintech")

# investList2 = [investList]
for iItem in investList:
	iItem.append("Investments")

# islambkList2 = [islambkList]
for isItem in islambkList:
	isItem.append("Islamic Banking")


# regulatList2 = [regulatList]
for rItem in regulatList:
	rItem.append("Regulations")


trendList = collabList+expanList+fintecList+investList+islambkList+regulatList
print (trendList[0:2])


#checking company name

for trendListItem in trendList:
	trendListTitle = trendListItem[0] # 0 is Title
	tokens = nltk.word_tokenize(trendListTitle)
	posTags = nltk.pos_tag(tokens)
	pT = [ ]
	for posTag in posTags:
		# print(posTag)
		if posTag[1] == 'NNP':
			pT.append(posTag[0])

	newsComp = " ".join(str(x) for x in pT)
	nsc = (newsComp)
	trendListItem.append(nsc)



print ("Before filtering redundants: "+str(len(trendList)))


# Removing redundants

filteredTrendsList = [ ]


for eachOne in trendList:
	# one_title1 = eachOne[0]
	# print (one_title1)


	if eachOne in filteredTrendsList:
		pass
	else:
		filteredTrendsList.append(eachOne)


print ("After filtering redundants: "+str(len(filteredTrendsList)))





# print(trendList[0])
# abcList = trendList[4:6]
# print (abcList)







#Export CSV
with open("iNSurtech_17.csv", 'w', encoding='utf-8', newline = '') as a:
    writer = csv.writer(a, delimiter = '#')
    
    for val in filteredTrendsList:
    	writer.writerow(val)
