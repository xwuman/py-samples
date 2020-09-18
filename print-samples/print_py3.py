# encoding:utf-8

s1 = "中文1"      # py3默认源码中常量字符串就是unicode类型
print(s1)         # py3的print是一个函数，只支持unicode类型
s2 = u"中文2"     # 效果和上面是一样
print(s2)       
s_utf = s1.encode('utf-8') # 
print(s_utf)
s_gbk = s2.encode('gbk')
print(s_gbk)
s_unicode = s_gbk.decode('gbk')
print(s_unicode)
print(type(s_gbk))
print(repr(s_gbk))