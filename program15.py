l=[1,2,3,4,5]
max=l[0]
min=l[0]
for i in l:
    if i>max:
        max=i
        if i<min:
            min=i
print(max)
print(min)
