# У меня закипели мозги пока я пыталась решить эту задачу.

string = 'rerorerorero'
string_end = 'kek'
i = 0
string_list=[]
string_end_list=[]
sure = True

for i in range(len(string)):
    string_list.append(string[i])
    i+=1
i = 0 

for i in range(len (string_end)):
    string_end_list.append(string_end[i])
    i+=1
i = 0
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