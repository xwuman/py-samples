#coding：utf-8
# python2默认的编解码方式是ASCII，所以如果有中文就要在文件头加上#coding：utf-8

s1 = "中文1"
print s1
s2 = u"中文2"
print(s2)
u1 = s1.decode('utf-8') # 通过decode，将utf-8编码转换为unicode；
print u1
g2 = s2.encode('gbk') # 通过encode可从unicode转换为gbk编码
print g2 # 只有这个才是正常的
