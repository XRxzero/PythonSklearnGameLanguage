fi = open("train_data(re).txt", "r", encoding='UTF-8')
str = fi.readline()
count=0
i=0
while (1):
    i+=1;
    str = fi.readline()
    if str == '': break
    str0 = str.split()[0]
    str1 = str.split()[1]
    str2 = ''
    k = 2
    while (str2 != '1' and str2 != '0'):
        str1 += ' ' + str2
        str2 = str.split()[k]
        k += 1
    if str2=='1':count+=1
print(count,i)
