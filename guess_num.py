"*练习, 随机整数猜数字"
#随机数字, 重复输入数字去猜, 对的话('终于猜对了'), 错的话('你的答案太大或太小')
import random
start = input('请输入你想输入的开始值: ')
end = input('请输入你想输入的结束值: ')
start = int(start)
end = int(end)

r = random.randint(start, end)
count = 0                            #count计数
while True:
	count = count + 1                #count += 1
	num = input('请猜数字: ')
	num = int(num)
	if num == r:
		print('哇, 你都猜了', count, '次了, 可算是猜对了！')
		break
	elif num > r:
		print('你的答案太大了')
	elif num < r:
		print('你的答案太小了')
	if count > 3 and count < 7:
		print('你已经试了', count, '次了！怎么还不对?')   
	elif count >= 7:
		print('很抱歉, 你没能在有效的次数内猜中答案, 游戏结束！！')
		break

