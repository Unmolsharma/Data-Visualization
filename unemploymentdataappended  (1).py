import csv

with open("unemploymentrate.csv") as csvFile: 
    reader = csv.reader(csvFile)
    inData = list(reader)

usableunemploymentdata=[]
employment = [0]

i=4
while i < len(inData):
    if inData[i][0] == "Canada":
        usableunemploymentdata.append(inData[i])
        yearsE = employment[0]
    i +=1

finalunemploymentdata = []

for data in usableunemploymentdata:
    for i in range(35):
        data.pop(0)
    data.remove("")
    for u in data:
        finalunemploymentdata.append(float(u))

print(finalunemploymentdata)
        
    

# for data in usableunemploymentdata:
#     for i in range(30):
#         data[i].remove()
        
    # print(data)

    


