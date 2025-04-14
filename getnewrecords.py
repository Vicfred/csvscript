import csv

with open('february.csv', 'r') as february:
    february_reader = csv.reader(february)
    february_records = set()
    headers = next(february_reader)
    print(headers)
    for row in february_reader:
        february_records.add((row[0], row[2]))
    new_records = set()
    with open('march.csv', 'r') as march:
        march_reader = csv.reader(march)
        next(march_reader)
        for row in march_reader:
            if (row[0], row[2]) not in february_records:
                print((row[0],row[2]))
                new_records.add(tuple(row))
    new_record_list = list(new_records)
    with open('new_records.csv', 'w', newline='') as output_file:
        writer = csv.writer(output_file)
        writer.writerow(headers)
        writer.writerows(new_record_list)
