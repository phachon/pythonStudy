#-------------------
# 第一个python game
#-------------------
print("hello python,这是我的第一个python程序")
guess = input("猜一下我在想哪个数字")
number = int(guess)
if number == 8:
	print("哦，你猜对了")
else:
	print("哦，你猜错了，真遗憾")
	print("再接再厉")
print("退出猜字游戏")
