import os
f = open('input.txt', 'r')
data = f.read().split('\n')
lst = []
cur = 0
for s in data:
	if s == '':
		lst.append(cur)
		cur = 0
	else:
		cur += int(s)
lst.sort()
print(sum(lst[-3:]))
