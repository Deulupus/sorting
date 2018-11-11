a = [2,4,5,6,2,9,4,2]
i = 1

for i in range(len(a)):
    element = a[i]
    j = i
    while j>0 and a[j-1] > element:
        a[j]=a[j-1]
        j=j-1
    a[j]=element

print(a)