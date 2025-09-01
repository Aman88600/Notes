import csv

# Open the CSV file
with open('Partial_ids/google.csv', mode='r', encoding='utf-8') as file:
    # Create a CSV reader object
    csv_reader = csv.reader(file)

    # Loop through the rows in the CSV
    for row in csv_reader:
        if "http" in row[0]:
            print(row[0])


import csv
# Open the CSV file
with open('Partial_ids/google.csv', mode='r', encoding='utf-8') as file:
    # Create a CSV reader object
    csv_reader = csv.reader(file)

    # Loop through the rows in the CSV
    scrape_lock = True
    for row in csv_reader:
        if "http" in row[0]:
            name = row[0].split("/")[-1]
            print(name)
            file=open(f"full_ids/{name}.txt", "r", encoding='utf-8')
            text = file.read()
            print(text)
            file.close()
# print(text['choices'][0]['message']['content'])
#Arrange the follwing content in a structured way in json format with following fields Basic Info Activity Exoerience Education Certification and Skills