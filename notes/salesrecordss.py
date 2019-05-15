import csv

List = []

with open("Sales Records.csv") as old_csv:
    reader = csv.reader(old_csv)
    total1 = 0
    for row in reader:
        if row[0] == 'Region':
            continue
        # old_number = int(row[0]) + 1
        old_number = row[13]
        if row[2] == 'Baby Food':
            total1 += float(old_number)
            # print(old_number)

print("The total baby food profit was:")
totalA = ("${:,}".format(round(total1, 2)))
print(totalA)
List.append(totalA)

with open("Sales Records.csv") as old_csv:
    reader = csv.reader(old_csv)
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
        if row[2] == 'Beverage':
            total2 += float(old_number)
            # print(old_number)
            total2 = round(total2, 2)
            totalB = ("${:,}".format(total2))
        if row[2] == 'Cereal':
            total3 += float(old_number)
            # print(old_number)
            total3 = round(total3, 2)
            totalC = ("${:,}".format(total3))
        if row[2] == 'Clothes':
            total4 += float(old_number)
            # print(old_number)
            total4 = round(total4, 2)
            totalD = ("${:,}".format(total4))
        if row[2] == 'Cosmetics':
            total5 += float(old_number)
            # print(old_number)
            total5 = round(total5, 2)
            totalE = ("${:,}".format(total5))
        if row[2] == 'Fruits':
            total6 += float(old_number)
            # print(old_number)
            total6 = round(total6, 2)
            totalF = ("${:,}".format(total6))
        if row[2] == 'Households':
            total7 += float(old_number)
            # print(old_number)
            total7 = round(total7, 2)
            totalG = ("${:,}".format(total7))
        if row[2] == 'Meat':
            total8 += float(old_number)
            # print(old_number)
            total8 = round(total8, 2)
            totalH = ("${:,}".format(total8))
        if row[2] == 'Office':
            total9 += float(old_number)
            # print(old_number)
            total9 = round(total9, 2)
            totalI = ("${:,}".format(total9))
        if row[2] == 'Personal':
            total10 += float(old_number)
            # print(old_number)
            total10 = round(total10, 2)
            totalJ = ("${:,}".format(total10))
        if row[2] == 'Snacks':
            total11 += float(old_number)
            # print(old_number)
            total11 = round(total11, 2)
            totalK = ("${:,}".format(total11))
        if row[2] == 'Vegetables':
            total12 += float(old_number)
            # print(old_number)
            total12 = round(total12, 2)
            totalL = ("${:,}".format(total12))

print("The total baby food profit was:")
totalA = ("${:,}".format(round(total1, 2)))
print(totalA)
List.append(totalA)

print("The total beverage profit was:")
totalB = ("${:,}".format(round(total2, 2)))
print(totalB)
List.append(totalB)

print("The total cereal profit was:")
totalC = ("${:,}".format(round(total3, 2)))
print(totalC)
List.append(totalC)

print("The total clothes profit was:")
totalD = ("${:,}".format(round(total4, 2)))
print(totalD)
List.append(totalD)

print("The total cosmetics profit was:")
totalE = ("${:,}".format(round(total5, 2)))
print(totalE)
List.append(totalE)

print("The total fruits profit was:")
totalF = ("${:,}".format(round(total6, 2)))
print(totalF)
List.append(totalF)

print("The total households profit was:")
totalG = ("${:,}".format(round(total7, 2)))
print(totalG)
List.append(totalG)

print("The total meat profit was:")
totalH = ("${:,}".format(round(total8, 2)))
print(totalH)
List.append(totalH)

print("The total office supplies profit was:")
totalI = ("${:,}".format(round(total9, 2)))
print(totalI)
List.append(totalI)

print("The total personal profit was:")
totalJ = ("${:,}".format(round(total10, 2)))
print(totalJ)
List.append(totalJ)

print("The total snacks profit was:")
totalK = ("${:,}".format(round(total11, 2)))
print(totalK)
List.append(totalK)

print("The total vegetables profit was:")
totalL = ("${:,}".format(round(total12, 2)))
print(totalL)
List.append(totalL)

print("The one who made the most profit was: ")
print(max(List))
