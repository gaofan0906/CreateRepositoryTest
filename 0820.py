

s='abbbccdfgk#'
i=0
c=1
while i<len(s)-1:
    for j in range(i+1,len(s)):
        if s[i]!=s[j]:
            break
        c+=1
    print(s[i])
    print(c)
    c=1
    i=j


import itertools

l = [(k, len(list(g))) for k, g in itertools.groupby('abbbccdfgk')]
