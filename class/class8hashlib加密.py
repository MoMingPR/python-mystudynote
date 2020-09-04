import hashlib
a = 'viax'
md5 = hashlib.md5()
md5.update(a.encode('utf-8'))
res = md5.hexdigest()
print('md5加密结果：',res)