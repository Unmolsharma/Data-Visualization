import csv
import matplotlib.pyplot as plt


with open("unemploymentrate.csv") as csvFile: 
    reader = csv.reader(csvFile)
    unData = list(reader)

with open("immigrants.csv") as csvFile: 
    reader = csv.reader(csvFile)
    imData = list(reader)


usableunemploymentdata=[]

i=4
while i < len(unData):
    print (i)
    if unData[i][0] == "Canada":
        usableunemploymentdata.append(unData[i])
    i +=1

for data in usableunemploymentdata:
    print(data)



usableimmigrantdata=[]

i=11
while i < len(imData):
    if imData[i][0] == "Immigrants 3":
        usableimmigrantdata.append(imData[i])
    i +=1

for data in usableimmigrantdata:
    print(data)

plt.plot(unData, imData)
plt.show()