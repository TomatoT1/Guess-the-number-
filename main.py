import random
secret = random.randint(1,50)
win = False
loss = False
play = True
Tries = 5
while play == True:
  while Tries > 0:
    print()
    guess = int(input("what's ur number guess?(0-50): "))
    Tries -= 1