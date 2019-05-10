import csv
with open("Sales Records.csv") as old_csv:
    reader = csv.reader(old_csv)
    total = 0
    for row in reader:
        if row[0] == 'Region':
            continue
        # old_number = int(row[0]) + 1
        old_number = row[13]
        if row[2] == 'Fruits':
            total += float(old_number)
            # print(old_number)
            total = round(total, 2)
            print("The total fruits profit was:")
            print("${:,}".format(total))
        if row[2] == 'Cosmetics':
            total += float(old_number)
            # print(old_number)
            total = round(total, 2)
            print("The total cosmetics profit was:")
            print("${:,}".format(total))
