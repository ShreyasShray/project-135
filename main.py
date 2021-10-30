# Importing required libraries
import csv
import matplotlib.pyplot as plt


# temporary list to store all data
temp_star_data = []


with open("final.csv") as f:
    csv_reader = csv.reader(f)
    for row in csv_reader:
        row.pop(0)
        temp_star_data.append(row)


# Lists to store headers and star_data
headers = temp_star_data[0]
star_data_rows = temp_star_data[1:]

# print(star_data_rows)


# Lists to store the different data of all stars
name = []
mass = []
radius = []
distance = []
gravity = []
for star_data in star_data_rows:
    name.append(star_data[0])
    mass.append(star_data[2])
    radius.append(star_data[3])
    distance.append(star_data[1])
    gravity.append(star_data[4])


# Checking the lengths of all data

# print(len(name))
# print(len(mass))
# print(len(radius))
# print(len(distance))
# print(len(gravity))
name.sort()
mass.sort()
radius.sort()
distance.sort()
gravity.sort()


# Ploting the graphs

# Name vs Mass
fig = plt.figure(figsize = (8, 6))
fig.subplots_adjust(bottom=0.44)
plt.bar(name, mass, color = "blue", width = 0.2)
plt.xlabel("name of the stars")
plt.xticks(rotation=45, ha='right')
plt.ylabel("mass of the stars")
plt.title("Star Name vs Mass")
plt.show()

# Name vs Radius
fig = plt.figure(figsize = (8, 6))
fig.subplots_adjust(bottom=0.44)
plt.bar(name, radius, color = "blue", width = 0.2)
plt.xlabel("name of the stars")
plt.xticks(rotation=45, ha='right')
plt.ylabel("radius of the stars")
plt.title("Star Name vs Radius")
plt.show()

# Name vs Distance
fig = plt.figure(figsize = (8, 6))
fig.subplots_adjust(bottom=0.44)
plt.bar(name, distance, color = "blue", width = 0.2)
plt.xlabel("name of the stars")
plt.xticks(rotation=45, ha='right')
plt.ylabel("distance of the stars")
plt.title("Star Name vs Distance")
plt.show()

# Name vs Gravity
fig = plt.figure(figsize = (8, 6))
fig.subplots_adjust(bottom=0.44, left = 0.25)
plt.bar(name, gravity, color = "blue", width = 0.2)
plt.xlabel("name of the stars")
plt.xticks(rotation=45, ha='right')
plt.ylabel("gravity of the stars")
plt.title("Star Name vs Gravity")
plt.show()