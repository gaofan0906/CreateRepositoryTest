# 0812
def rev(s):
    i = 0
    j = len(s) - 1
    slist = list(s)
    while (i < j):
        temp = slist[i]
        slist[i] = slist[j]
        slist[j] = temp
        i += i
        j -= j
    s2 = ''.join(slist)
    return s2


rev('hello')
