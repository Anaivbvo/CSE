import csv

with open("Book1.csv") as old_csv:
    with open("MyNewFile.csv", 'w', newline='') as new_csv:
        print("Writing file..... ")
        reader = csv.reader(old_csv)
        writer = csv.writer(new_csv)
        for row in reader:
            old_number = row[0]
            new_number = old_number + 1
            row[0] = new_number
            writer.wirterow(row)
            # print(int(old_number) + 1)
            print(old_number)
            print("OK")
