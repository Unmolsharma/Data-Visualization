import csv

with open("dc.csv") as dcdata: 
    reader = csv.reader(dcdata)
    dcList = list(reader)


with open("marvel.csv") as marveldata: 
    reader = csv.reader(marveldata)
    marvelList = list(reader) 

allimmigrants = []
dcwomen = []
marvelwoman = []
dcprocessed = []

i=0
dcwomen=[]
while i < len(dcList):
    if dcList[i][4] == "Good Characters" and dcList[i][7] == "Female Characters" and dcList[i][9] == "Living Characters" :
       allimmigrants.append([dcList[i][1], dcList[i][3], 'DC'])
    i += 1
   
i=0
marvelwomen=[]
while i < len(marvelList):
    if marvelList[i][4] == "Good Characters" and marvelList[i][7] == "Female Characters" and marvelList[i][9] == "Living Characters" :
       allimmigrants.append([marvelList[i][1], marvelList[i][3], 'Marvel'])
    i += 1
       

for female in allimmigrants:
    print(female)

print (len(allimmigrants))

countJobs = 0
i= 0
while i <len(allimmigrants):
    if allimmigrants [i][1] == "Job Vacancies":
        countJobs += 1
    i +=1

print (countJobs)
    