import random

r = random.randint(1, 100)

while True:
	n = input('請輸入輸字（1~100）: ')
	n = int(n)
	if r == n:
		print('終於猜對了')
		break
	elif r > n:
		print('比答案小')
	elif r < n:
	    print('比答案大')
	else:
	    print('請從 1~100 中輸入一個數字')	

