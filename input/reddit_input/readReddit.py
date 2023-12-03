import json
import datetime
import tqdm

# @title JSON Key Values
json_keys = {
  'time': 'created_utc',
  'title':'title',
  'text': 'selftext',
  'id': 'id',
  'link_path': 'permalink',
  'author':'author',
  'score':'score',
  'ups':'ups',
  'downs':'downs',
  'retrived_on':'retrieved_on'
}


# Open the JSON file for reading
filtered_data = []
with open('argentina_submissions.json', 'r') as file:
    for line in tqdm.tqdm(file):

        # Process each line here
        json_data = json.loads(line)
        
        for key in json_keys:
            key = json_data.gey(json_keys[key],'')
            
        
        timestamp = datetime.datetime.fromtimestamp(int(time))
        year, month, day = timestamp.strftime('%Y-%m-%d').split('-')
        id = json_data.get(json_keys['id'],'')
        created_utc = json_data.get(json_keys['time'],'')
        title = json_data.get(json_keys['title'],'')
        text = json_data.get(json_keys['text'],'')
        link_path = json_data.get(json_keys['link_path'],'')
        
        timestamp = datetime.datetime.fromtimestamp(int(time))
        year, month, day = timestamp.strftime('%Y-%m-%d').split('-')

        # Format the datetime object as "YYYY MM DD"
        # formatted_date = timestamp.strftime("%Y %m %d")
        if 1514764801 <= int(created_utc) <= 1672531199 :       
            try:
                filtered_data.append([id,year,month,day,?title, text, link_path])
                #filtered_data.append([created_utc,data['body']])
            except:
                continue



import csv

with open('filtered_file.csv', mode='w') as _file:
    _writer = csv.writer(_file, delimiter=',')
    for data in filtered_data:
        _writer.writerow(data)
