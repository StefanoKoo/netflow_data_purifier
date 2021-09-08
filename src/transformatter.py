import datetime

def string_to_date(string):
    
    return datetime.datetime.strptime(string, '%Y-%m-%d %H:%M:%S')


