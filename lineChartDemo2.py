import matplotlib.pyplot as plt
import csv
import numpy as np
import pandas as pd

 



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


combinedlist = []
sum = 0
count = 0
for i in finalimmigrantdata:
    if count != 4 or count >= 4:
        sum += i
        count += 1
    if count == 4:
        combinedlist.append(sum)
        sum = 0
        count = 0

    

combinedlist = []
sum = 0
count = 0
for i in finalimmigrantdata:
    if count != 4 or count >= 4:
        sum += i
        count += 1
    if count == 4:
        combinedlist.append(sum)
        sum = 0
        count = 0



with open("unemploymentrate.csv") as csvFile: 
    reader = csv.reader(csvFile)
    inData = list(reader)

usableunemploymentdata=[]
employment = [0]

i=4
while i < len(inData):
    if inData[i][0] == "Canada":
        usableunemploymentdata.append((inData[i]))
        yearsE = employment[0]
    i +=1

finalunemploymentdata = []

for data in usableunemploymentdata:
    for i in range(35):
        data.pop(0)
    data.remove("")
    for u in data:
        finalunemploymentdata.append(float(u))
    



z = np.polyfit(combinedlist,finalunemploymentdata, 1)
p = np.poly1d(z)

plt.plot(combinedlist,p[combinedlist], linewidth = 4)


plt.scatter(combinedlist,finalunemploymentdata)
plt.title("Changing Of Unemployment Rate Based On Population Of New Immigrants In Canada 1990-2020")
plt.xlabel("Population Of New Immigrants")
plt.ylabel("Unemployment Rate")
plt.show()
