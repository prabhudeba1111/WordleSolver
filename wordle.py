import enchant

Dic = enchant.Dict("en_US")
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#print (len(alphabets))
used = []
left = [x for x in alphabets if x not in used]
# print(left)
ret = []
idx = 1
for i in left:
    for j in left:
        for k in left:
            for l in left:
                for m in left:
                    word = [i, j, k, l, m]
                    new = ''.join(word)
                    if Dic.check(new):
                        ret.append(new)
                        print(idx)
                        idx += 1


print(len(ret))
print (ret)

with open('dictionary.txt', 'w') as f:
    for word in ret:
        f.write(word+'\n')

txt = []
with open('dictionary.txt', 'r') as f:
    for word in f:
        txt.append(word.strip())

print(txt)

# nxt = [word for word in ret if 'n' in word]
# print (nxt)