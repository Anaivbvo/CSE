import csv

topics = ['baby food', 'beverage', 'cereal', 'clothes', 'cosmetics', 'fruits', 'households', 'meat', 'office supplies',
          'personal', 'snacks', 'vegetables']


with open("Sales Records.csv") as old_csv:
    reader = csv.reader(old_csv)
    total1 = 0
    total2 = 0
    total3 = 0
    total4 = 0
    total5 = 0
    total6 = 0
    total7 = 0
    total8 = 0
    total9 = 0
    total10 = 0
    total11 = 0
    total12 = 0
    for row in reader:
        if row[0] == 'Region':
            continue
        # old_number = int(row[0]) + 1
        old_number = row[13]
        if row[2] == topics[0]:
            total1 += float(old_number)
            # print(old_number)
            total1 = round(total, 2)
            totalA = ("${:,}".format(total))
        if row[2] == topics[1]:
            total += float(old_number)
            # print(old_number)
            total = round(total, 2)
            total1 = ("${:,}".format(total))
        if row[2] == topics[2]:
            total += float(old_number)
            # print(old_number)
            total = round(total, 2)
            total1 = ("${:,}".format(total))
        if row[2] == topics[3]:
            total += float(old_number)
            # print(old_number)
            total = round(total, 2)
            total1 = ("${:,}".format(total))
        if row[2] == topics[4]:
            total += float(old_number)
            # print(old_number)
            total = round(total, 2)
            total1 = ("${:,}".format(total))
        if row[2] == topics[5]:
            total += float(old_number)
            # print(old_number)
            total = round(total, 2)
            total1 = ("${:,}".format(total))
        if row[2] == topics[6]:
            total += float(old_number)
            # print(old_number)
            total = round(total, 2)
            total1 = ("${:,}".format(total))
        if row[2] == topics[7]:
            total += float(old_number)
            # print(old_number)
            total = round(total, 2)
            total1 = ("${:,}".format(total))
        if row[2] == topics[8]:
            total += float(old_number)
            # print(old_number)
            total = round(total, 2)
            total1 = ("${:,}".format(total))
        if row[2] == topics[9]:
            total += float(old_number)
            # print(old_number)
            total = round(total, 2)
            total1 = ("${:,}".format(total))
        if row[2] == topics[10]:
            total += float(old_number)
            # print(old_number)
            total = round(total, 2)
            total1 = ("${:,}".format(total))
        if row[2] == topics[11]:
            total += float(old_number)
            # print(old_number)
            total = round(total, 2)
            total1 = ("${:,}".format(total))

print("The total fruits profit was:")

