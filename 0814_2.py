# 字符串 We Are Happy替换空格We%20Are%20Happy
# 简单实现
# 将字符串转为列表，循环替换空格，再转回字符串输出
'''str='We Are Happy'
str2list=list(str)
print(str2list)
for i in range(len(str2list)):
    if str2list[i]==' ':
        str2list[i]='%20'

s=''.join(str2list)
print(s)'''


# 写成函数
def replaceSpace(s):
    if type(s) != str:
        return
    str2list = list(s)
    new_s = []
    for i in str2list:  # 直接循环列表
        if i == ' ':
            new_s.append('%')
            new_s.append('2')
            new_s.append('0')
        else:
            new_s.append(i)

    return ''.join(new_s)


s = 'We Are Happy'
print(replaceSpace(s))
