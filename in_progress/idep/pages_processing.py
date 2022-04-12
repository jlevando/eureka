import csv
import json

#function to get all headers in DLCS export csv and then add three from eureka csv
def get_headers(file_name):
    with open(file_name, 'r', newline='') as f:
        r = csv.reader(f, delimiter=',')
        headers = next(r)
        return headers

works_csv = str(input('Works CSV path:')).strip(" ")
pages_csv = str(input('Pages CSV path:')).strip(" ")
works_dict = {}

cursor = csv.DictReader(open(works_csv),
    delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)

for row in cursor:
    item_ark = row['Item ARK']
    parent_ark = row['Parent ARK']
    object_type = row['Object Type']
    pagination = row['viewingHint']
    sequence = row['Item Sequence']
    works_dict[item_ark] = {
            'Parent ARK': parent_ark,
            'Object Type': object_type,
            }
#new csv for each work's pages
for item_ark in works_dict.keys():
    if works_dict[item_ark]['Object Type'] == 'Work':
        pages_file_name = str((str(item_ark)).replace('ark:/', '').replace('/', '')+'_pages.csv')
        with open(pages_file_name, 'w') as out:
            writer = csv.DictWriter(out, fieldnames=get_headers(pages_csv))
            writer.writeheader()
            cursor = csv.DictReader(open(pages_csv),
            delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
            for row in cursor:
                if row['Parent ARK'] == item_ark:
                    writer.writerow(row)
                else:
                    pass
