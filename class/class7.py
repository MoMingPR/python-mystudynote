#读取文件
file_1 = open('地址','r',encoding='utf-8')
filecontent = file_1.read()
print(filecontent)
file_1.close()
#添加
file_1 = open('地址','a',encoding='utf-8')
file_1.write('addtext')
file_1.close()
#写入文件
file_1 = open('地址','w',encoding='utf-8')
file_1.write('addtext')