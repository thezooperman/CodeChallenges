string = '(())'
opencount = 0
closecount = 0
count = 0
for i in string:
    if i == '(':
        opencount += 1
    elif i == ')':
        closecount += 1
    if opencount == closecount:
        count = opencount
    else:
        count = closecount
print(count)
