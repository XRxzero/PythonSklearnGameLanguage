fi = open("train_data.txt", "r", encoding='UTF-8')
i = 0
str = fi.readline()
fo = open("train_data(re).txt", "w", encoding='UTF-8')
fo.write('qid\ttext\tlabel\n')
str_fuck_list = ['nm', 'tm', 'fw', 'laji', 'sb', 'zz', '低能', '全家', '你爸', '尼玛', '鸡', '干嘛', '曰', '草', '艹', '傻', 'sha',
                 'Sha','废物','辣鸡','啥比',
                 '演', '挂', '送', '投']
str_good_list = ['皮肤', '别挂', '别送', '别投', '别演', '不要送', '不要挂', '不要投', '不要演','表演']
gai = 0
while (1):
    i += 1
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
        fucked = False
    for j in range(len(str_fuck_list)):
        if (str1.find(str_fuck_list[j]) >= 0):
            fucked = True
            if (str2 == '0'):
                str2 = '1'
                gai += 1
                break

    for j in range(len(str_good_list)):
        if (str2 == '1'):
            if (str1.find(str_good_list[j]) >= 0):
                str2 = '0'
                gai -= 1
                break
    if (str2 == '1'):
        if (not fucked):
            str2 = '0'
            gai -= 1

    str3 = str0 + '\t' + str1 + '\t' + str2 + '\n'
    fo.write(str3)
print(gai)
