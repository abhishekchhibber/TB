import re
import csv

with open("uae_preschool_text.txt", "r") as file: # this file should have combined text of all the PDFs
	content = file.read()

extractedList = [ ]
eRegex = re.compile(r'[a-zA-Z._0-9]+@\w+\.[a-zA-Z._0-9]+')
result = eRegex.findall(content) 
# coolResult = '\n'.join(result) 
if len(result) != 0:
	for resOne in result:
		resTwo = resOne
		extractedList.append(resTwo)

print ("Total Emails: "+str(len(extractedList)))


finalList = [ ]

for extract in extractedList:
	if extract in finalList:
		pass
	else:
		finalList.append(extract)


print ("Final Emails: "+str(len(finalList)))

#Export CSV
with open("uae_preschool_emails.csv", 'w') as a: # .csv file for extracting the results
    writer = csv.writer(a)
    
    for val in finalList:
    	writer.writerow(val)
