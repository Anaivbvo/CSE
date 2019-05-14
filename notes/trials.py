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
            total1 = round(total1, 2)
            totalA = ("${:,}".format(total1))
        if row[2] == topics[1]:
            total2 += float(old_number)
            # print(old_number)
            total2 = round(total2, 2)
            totalB = ("${:,}".format(total2))
        if row[2] == topics[2]:
            total3 += float(old_number)
            # print(old_number)
            total3 = round(total3, 2)
            totalC = ("${:,}".format(total3))
        if row[2] == topics[3]:
            total4 += float(old_number)
            # print(old_number)
            total4 = round(total4, 2)
            totalD = ("${:,}".format(total4))
        if row[2] == topics[4]:
            total5 += float(old_number)
            # print(old_number)
            total5 = round(total5, 2)
        if row[2] == topics[5]:
            total6 += float(old_number)
            # print(old_number)
            total6 = round(total6, 2)
        if row[2] == topics[6]:
            total7 += float(old_number)
            # print(old_number)
            total7 = round(total7, 2)
        if row[2] == topics[7]:
            total8 += float(old_number)
            # print(old_number)
            total8 = round(total8, 2)
        if row[2] == topics[8]:
            total9 += float(old_number)
            # print(old_number)
            total9 = round(total9, 2)
        if row[2] == topics[9]:
            total10 += float(old_number)
            # print(old_number)
            total10 = round(total10, 2)
        if row[2] == topics[10]:
            total11 += float(old_number)
            # print(old_number)
            total11 = round(total11, 2)
        if row[2] == topics[11]:
            total12 += float(old_number)
            # print(old_number)
            total12 = round(total12, 2)

print("The total baby food profit was:")
print(totalA)
print("The total beverage profit was:")
print("The total cereal profit was:")
print("The total clothes profit was:")
print("The total cosmetics profit was:")
print("The total fruits profit was:")
print("The total households profit was:")
print("The total meat profit was:")
print("The total office supplies profit was:")
print("The total personal profit was:")
print("The total snacks profit was:")
print("The total vegetables profit was:")


