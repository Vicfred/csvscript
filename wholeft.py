import csv

with open('march.csv', 'r') as march:
    march_reader = csv.reader(march)
    march_headers = next(march_reader)
    march_ids = set()
    for row in march_reader:
        march_ids.add(row[0])
    who_left = set()
    with open('february.csv', 'r') as february:
        february_reader = csv.reader(february)
        february_headers = next(february_reader)
        for row in february_reader:
            if row[0] not in march_ids:
                print(row[0], "left")
                who_left.add(tuple(row))
    new_record_list = list(who_left)
    new_record_list.sort(key=lambda x: x[0])
    with open('peole_who_left.csv', 'w', newline='') as output_file:
        writer = csv.writer(output_file)
        writer.writerow(march_headers)
        writer.writerows(new_record_list)
