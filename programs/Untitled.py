import json
import datetime
import tqdm
import csv
import os
import pandas as pd

# @title JSON Key Values
json_keys = {
  'time': 'created_utc',
  'id': 'id',
  'link_path': 'permalink',
  'title':'title',
  'texts': {'text':'selftext','title':'title'}
}

def json_chunks_processing(large_filename, json_keys):
  file = os.path.splitext(large_filename)[0] #without the .json
  # Directory where the JSON files are located
  json_files_dir = f'../input/reddit_input/{file}-split_data/'

  # Directory where the CSV file is located
  csv_table_dir = output_dir + f'{file}-output_table.csv'

  with open(csv_table_dir, 'w') as csv_file: # Check if the CSV file is empty
    csv_empty = os.path.getsize(csv_table_dir) == 0

    if csv_empty:
      # If the file is empty, write the headers
      columns = []
      for key in json_keys['texts']:    
        columns.append(key)
      columns = ['id', 'year', 'month', 'day']+columns+['permalink']
      pd.DataFrame(columns=columns).to_csv(csv_file, index=False, header=True, sep=',')

  for filename in os.listdir(json_files_dir): # Loop through all files in the specified folder
    if filename.endswith('.json'):
      data_chunk = [] # Initialize an empty list to hold the data for this file
      with open('argentina_submissions.json', 'r') as file:
        for line in tqdm.tqdm(file):
          # Process each line here
          json_data = json.loads(line)
          row = []

          for key in json_keys['texts']:
            value = json_data.get(json_keys[key],'')
            row.append(value)
          
          id = json_data.get(json_keys['id'],'')
          created_utc = json_data.get(json_keys['time'],'')
          link_path = json_data.get(json_keys['link_path'],'')
          timestamp = datetime.datetime.fromtimestamp(int(created_utc))
          year, month, day = timestamp.strftime('%Y-%m-%d').split('-')
          
          row = [id, year, month, day]+row+[link_path]
          # Format the datetime object as "YYYY MM DD"
          # formatted_date = timestamp.strftime("%Y %m %d")
          if 1514764801 <= int(created_utc) <= 1672531199 :       
            try:
              data_chunk.append(row)
            except:
              continue

      with open('filtered_file.csv', mode='a', newline='') as _file:
        _writer = csv.writer(_file, delimiter=',')
        for data in data_chunk:
            _writer.writerow(data)

      data_chunk = []      