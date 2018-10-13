# У меня закипели мозги пока я пыталась решить эту задачу.

string = 'rerorerorero'
string_end = 'kek'
sure = True

string_list=[ i for i in string]
string_end_list=[ i for i in string_end]

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
