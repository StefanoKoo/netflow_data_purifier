import csv
import json
import transformatter

original_data = open('../data/flows_6.csv','r',encoding='utf-8')
reader = csv.reader(original_data)

purified_data = open('../data/data.csv', 'w', encoding='utf-8')
writer = csv.writer(purified_data)
writer.writerow(['TIME','IPV4_SRC_ADDR','IPV4_DST_ADDR','NEXT_HOP','INPUT','OUTPUT','IN_PACKETS','IN_OCTETS','FIRST_SWITCHED','LAST_SWITCHED','SRC_PORT','DST_PORT',
'TCP_FLAGS','PROTO','TOS','SRC_AS','DST_AS','SRC_MASK','DST_MASK'])

with open('../config/config_date.json', 'r' , encoding='utf-8') as json_file:
    config = json.load(json_file)

start_time = transformatter.string_to_date(config['Start']['Date'] + ' ' + config['Start']['Time'])
end_time = transformatter.string_to_date(config['End']['Date'] + ' ' + config['End']['Time'])

for line in reader:
    if line[0] == 'TIME':
        continue

    standard_date = transformatter.string_to_date(line[0])

    if (start_time > standard_date) :
        continue
    elif (end_time < standard_date) :
        break
    else:
        writer.writerow(line)
        
original_data.close
purified_data.close