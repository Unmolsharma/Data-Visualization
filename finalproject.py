import matplotlib.pyplot as plt
import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Open the immigrants csv file and read it
with open("immigrants.csv") as csvFile: 
    reader = csv.reader(csvFile)
    inData = list(reader)

# Initialize empty lists to store the immigrant data and the years data
usableimmigrantdata=[]
yearsdata = []

# Append the immigrant data to the usableimmigrantdata list
if inData[11][0] == "Immigrants 3":
    usableimmigrantdata.append(inData[11])

# Append the years data to the yearsdata list
if inData[9][0] == "Components of population growth":
    yearsdata.append(inData[9])

# Remove the first element from the immigrant data
usableimmigrantdata[0].remove("Immigrants 3")

# Initialize an empty list to store the final immigrant data
finalimmigrantdata = []

# Iterate through the immigrant data and convert each value to an integer
for i in usableimmigrantdata:
    for j in i:
        new_data = int(j.replace(",", ''))
        finalimmigrantdata.append(new_data)

# Initialize an empty list to store the combined data
combinedlist = []

# Initialize variables to keep track of the sum and count
sum = 0
count = 0

# Iterate through the final immigrant data and combine every four values
for i in finalimmigrantdata:
    if count != 4 or count >= 4:
        sum += i
        count += 1
    if count == 4:
        combinedlist.append([sum])
        sum = 0
        count = 0

# Open the unemployment rate csv file and read it
with open("unemploymentrate.csv") as csvFile: 
    reader = csv.reader(csvFile)
    inData = list(reader)

# Initialize an empty list to store the unemployment data
usableunemploymentdata=[]

# Initialize a list to store the employment data
employment = [0]

# Iterate through the inData list and append the unemployment data for Canada to the usableunemploymentdata list
i=4
while i < len(inData):
    if inData[i][0] == "Canada":
        usableunemploymentdata.append((inData[i]))
        yearsE = employment[0]
    i +=1

# Initialize an empty list to store the final unemployment data
finalunemploymentdata = []

# Iterate through the unemployment data and convert each value to a float
for data in usableunemploymentdata:
    for i in range(35):
        data.pop(0)
    data.remove("")
    for u in data:
        finalunemploymentdata.append(float(u))

# Convert combinedlist to a 1D array
combinedlist = np.array(combinedlist).flatten()

# Fit a polynomial to the data and create a function to plot the trendline
z = np.polyfit(combinedlist,finalunemploymentdata, 1)
p = np.poly1d(z)

# Set the background color of the figure to red and white
plt.figure().set_facecolor("red")

# Set the background color of the graph to blue
plt.gca().set_facecolor("blue")

# Plot the trendline
plt.plot(combinedlist, p(combinedlist), linewidth = 4,linestyle= "--", color=(0.5, 0.8, 0.5))

# Plot the scatter plot
plt.scatter(combinedlist,finalunemploymentdata, color="orange")
plt.title("Changing Of Unemployment Rate Based On Population Of New Immigrants In Canada 1990-2020")
plt.xlabel("Population Of New Immigrants")
plt.ylabel("Unemployment Rate")
plt.show()



