import csv

with open("immigrants.csv") as csvFile: 
    reader = csv.reader(csvFile)
    inData = list(reader)

usableimmigrantdata=[]
yearsdata = []


if inData[11][0] == "Immigrants 3":
    usableimmigrantdata.append(inData[11])

if inData[9][0] == "Components of population growth":
    yearsdata.append(inData[9])

usableimmigrantdata[0].remove("Immigrants 3")

finalimmigrantdata = []
for i in usableimmigrantdata:
    for j in i:
        new_data = int(j.replace(",", ''))
        finalimmigrantdata.append(new_data)

print(len(finalimmigrantdata))
   
    

