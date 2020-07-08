"*练习, 随机整数猜数字"
#随机1-100, 重复输入数字去猜, 对的话('终于猜对了'), 错的话('你的答案太大或太小')
import random
r = random.randint(1, 100)
while True:
	num = input('请猜数字: ')
	num = int(num)
	if num == r:
		print('终于猜对了！')
		break
	elif num > r:
		print('你的答案太大了')
	elif num < r:
		print('你的答案太小了')
