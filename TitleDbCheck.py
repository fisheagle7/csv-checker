import csv

titles = set()
dbtitles = set()

with open('Favorite TV Shows - Form Responses 1 (1).csv', 'r') as file:
    #create the reader
    reader = csv.DictReader(file)
    #skip the first line
    # Iterate over the csv file
    for row in reader:
        titles.add(row["title"].strip().upper())

with open('dbtitles.csv', 'r') as dbfile:
    #create the reader
    dbreader = csv.DictReader(dbfile)

    #iteratite over the csv file
    for row in dbreader:
        dbtitles.add(row["title"])

print("User Input")

for title in titles:
    print(f"{title}")

print("\n")

print("Movie Database")
for title in dbtitles:
    print(f"{title}")

print("\n")

print("Is the user input a valid title:")
for title in titles:
    if title in dbtitles:
        print(f"{title} > valid")
    else:
        print(f"{title} > invalid")



