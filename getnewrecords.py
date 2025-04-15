import csv

with open('february.csv', 'r') as february:
    february_reader = csv.reader(february)
    february_records = set()
    february_ids = set()
    for row in february_reader:
        february_records.add((row[0], row[2]))
        february_ids.add(row[0])
    new_records = set()
    with open('march.csv', 'r') as march:
        march_reader = csv.reader(march)
        headers = next(march_reader)
        headers.append("new id?")
        for row in march_reader:
            if (row[0], row[2]) not in february_records:
                print((row[0],row[2]))
                if(row[0] not in february_ids):
                    row.append("new id")
                else:
                    row.append("old id")
                new_records.add(tuple(row))
    new_record_list = list(new_records)
    new_record_list.sort(key=lambda x: x[0])
    print(new_record_list)
    with open('new_records.csv', 'w', newline='') as output_file:
        writer = csv.writer(output_file)
        writer.writerow(headers)
        writer.writerows(new_record_list)
