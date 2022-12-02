import os

def mySplit(x):
	return x.split(' ')

f = open('input.txt', 'r')
data = list(map(mySplit, f.read().split('\n')))[:5]
hand = {"X": 1, "Y": 2, "Z": 3}
hand2 = {"A": 1, "B": 2, "C": 3}
lose = {"A" : "Z", "B": "X", "C": "Y"}
win = {"A": "Y", "B": "Z", "C": "X"}
ans = 0
# part 1
# for you, me in data:
# 	a, b = ord(you) - ord('A'), ord(me) - ord('X')
# 	print(a, b)
# 	if a == b:
# 		ans = ans + hand[me] + 3
# 	elif a - b > 1 :
# 		if a - b == 1:
# 			ans = ans + hand[me]
# 		else:
# 			ans = ans + hand[me] + 6
# 	else: 
# 		if a - b == -1:
# 			ans = ans + hand[me] + 6
# 		else:
# 			ans = ans + hand[me]
# part 2
print(data)
for you, res in data:
	if res == "X":
		ans = ans + hand[lose[you]]		
	elif res == "Y":
		ans = ans + 3 + hand2[you]
	else:
		ans = ans + 6 + hand[win[you]]

print(ans)
