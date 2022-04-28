"""checks if all combination of paswords have a unique caharacter"""
def check(x):
    re = True
    for i in x:
        count_f = x.count(i)
        if count_f > 1:
            re = False
    return re
array = []
#creating 5-digit password
for i1 in range(0, 9):
    for i2 in range(0, 9):
        for i3 in range(0, 9):
            for i4 in range(0,9):
                for i5 in range(0,9):
                    x = [i1,i2,i3,i4,i5]
                    if check(x):
                        y =f'{i1}{i2}{i3}{i4}{i5}'
                        array.append(y)
                        
if check(array):
    print('all unique')
else:
    print('not all unique')
