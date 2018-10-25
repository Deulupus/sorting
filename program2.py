def foo(string):
    str_list= [ i for i in string]
    return str_list
string = 'rerorerorero'
string_end = 'kek'
sure = True

string_list=foo(string)
string_end_list=foo(string_end)

reverse_string = string_list[::-1]
reverse_end = string_end_list[::-1]

for i in range(len(string_end)):
    if reverse_string[i] == reverse_end[i]:
        continue
    else:
        sure = False
    
if sure == True:
    print('True')
else:
    print('False')
