import random
r = random.randint(1, 100)
while True:
    guess = input('請輸入一個數字')
    guess = int(guess)
    if guess == r:
        print('恭喜你答對了')
        break
    elif guess > r:
    	print('你猜得太大了，請再猜一次')
    else:
    	print('你猜得太小了，請再猜一次')