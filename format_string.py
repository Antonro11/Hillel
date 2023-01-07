def format_string(string):
    string_to_lst = [item for item in string]
    count =len(string)
    while count > 3:
        count-=3
        string_to_lst.insert(count,'.')
    result = ''
    for i in string_to_lst:
        result+=i
    return result
  
  
print(format_string('10000000'))
  
  
