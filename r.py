import random
start = (input('請決定隨機數字範圍開始值:'))
end = input('請決定隨機數字範圍結束值:')
r = random.randint(int(start), int(end))
count = 0
while True:
	count += 1
	n = input('請輸入數字：')
	n = int(n)
	if r == n:
		print('終於猜對了')
		print('總共猜了', count, '次')
		break
	elif r > n:
		print('比答案小')
	elif r < n:
	    print('比答案大')
	else:
	    print('請從 1~100 中輸入一個數字')	

