import random
r = random.randint(1, 100)
count = 0
while True:
    count += 1
    guess = input('請輸入一個數字')
    guess = int(guess)
    if guess == r:
        print('恭喜你答對了')
        break
    elif guess > r:
    	print('你猜得太大了，請再猜一次')
    else:
    	print('你猜得太小了，請再猜一次')
    print('這是你猜的第', count,'次')