import json
from datetime import datetime
import tqdm
# Open the JSON file for reading
filtered_data = []
with open('PremierLeague_comments', 'r') as file:
    for line in tqdm.tqdm(file):
        # Process each line here
        data = json.loads(line) 
        created_utc = data['created_utc']
        timestamp = datetime.utcfromtimestamp(int(created_utc))
        # Format the datetime object as "YYYY MM DD"
        formatted_date = timestamp.strftime("%Y %m %d")
        if int(created_utc) >1609471889:        # Unix Time ~ 1/1/2021
            filtered_data.append([created_utc,data['body']])



import csv

with open('filtered_file.csv', mode='w') as _file:
    _writer = csv.writer(_file, delimiter=',')
    for data in filtered_data:
        _writer.writerow(data)

