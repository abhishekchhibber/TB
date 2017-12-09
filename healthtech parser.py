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
path =  "F:\\April-2017\\healthtech_apr\\HTML" # Set path of new directory here
os.chdir(path)
new_d = os.getcwd() 
print ("New directory: ",new_d)
dir_file_list = os.listdir(path)
print (len(dir_file_list))





# 1 Read saved HTML pages + Get all the attributs + Sort in individual lists

collabList = [ ]
expanList = [ ]
investList = [ ]
regulatList = [ ]
newProductList = [ ]

for s in dir_file_list: 
	
	print (s)
	file = open(s, encoding="utf8")
	content = file.read()

	bsObj = BeautifulSoup(content, "html5lib")

	items  = bsObj.findAll("div",{"class":"g"})

	for item in items:

		title = item.h3.text
		link = item.a['href']
		datez = item("span",{"class":"f nsa _QHs"})
		dateFinal = datez[0].text
		source = item("span",{"class":"_OHs _PHs"})
		sourceFinal = source[0].text
		snippet = item("div",{"class":"st"})
		snippetFinal = snippet[0].text

		result = [title,snippetFinal,link,dateFinal,sourceFinal]
		# rowTitle = title+snippetFinal
		rowTitle = title


		if "tie-up" in rowTitle or "partner" in rowTitle or "collaborate" in rowTitle or "collaboration" in rowTitle or "partners" in rowTitle or "ties-up" in rowTitle or "mou" in rowTitle or "merge" in rowTitle or "ties up" in rowTitle:
			collabList.append(result)
		if "IPO" in rowTitle or "rebrand" in rowTitle or "opens" in rowTitle or "expand" in rowTitle or "open" in rowTitle or "grow" in rowTitle or "to open" in rowTitle or "expansion" in rowTitle:
			expanList.append(result)
		if "raise" in rowTitle or "stake" in rowTitle or "million" in rowTitle or "picks" in rowTitle or "bags" in rowTitle or "funding" in rowTitle or "sells" in rowTitle or "acquire" in rowTitle or "invest" in rowTitle or "raise" in rowTitle or "sell" in rowTitle or "raising" in rowTitle or "merge" in rowTitle:
			investList.append(result)
		if "governance" in rowTitle or "licence" in rowTitle or "permit" in rowTitle or "IMF" in rowTitle or "bailout" in rowTitle or "regulator" in rowTitle or "government" in rowTitle or "federal" in rowTitle or "privatisation" in rowTitle or "privatization" in rowTitle or "law" in rowTitle or "regualtion" in rowTitle:
			regulatList.append(result) 
		if "launch" in rowTitle or "introduce" in rowTitle or "opens" in rowTitle or "to open" in rowTitle or  "launched" in rowTitle or "brings" in rowTitle or "start" in rowTitle: 
			newProductList.append(result) 

	time.sleep(1)

print("Collaboration: ",len(collabList))
print("expansion: ",len(expanList))
print("investment: ",len(investList))
print("New Products: ",len(newProductList))
print("regualtions: ", len(regulatList))

sumIndexed  = len(collabList)+len(expanList)+len(newProductList)+len(investList)+len(regulatList)

print("Total Indexed: ",sumIndexed)

# Adding trend name
# collabList2 = collabList
for cItem in collabList:
	cItem.append("Collaboration")

# expanList2 = [expanList]
for eItem in expanList:
	eItem.append("Expansion")


for fItem in newProductList:
	fItem.append("New Products")

# investList2 = [investList]
for iItem in investList:
	iItem.append("Investments")

# regulatList2 = [regulatList]
for rItem in regulatList:
	rItem.append("Regulations")


trendList = collabList+expanList+newProductList+investList+regulatList
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
	if eachOne in filteredTrendsList:
		pass
	else:
		filteredTrendsList.append(eachOne)


print ("After filtering redundants: "+str(len(filteredTrendsList)))




# print(trendList[0])
# abcList = trendList[4:6]
# print (abcList)







#Export CSV
with open("healthtechApr-2017.csv", 'w', encoding='utf-8', newline = '') as a: # in the new directory path
    writer = csv.writer(a, delimiter = '#')
    
    for val in filteredTrendsList:
    	writer.writerow(val)
