def format_records_dict(records):
    return '<br>'.join(str(key)+' '+str(value) for key,value in records.items())

def format_records_lst(records):
    return '<br>'.join(str(record) for record in records)

