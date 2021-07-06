import random
secret = random.randint(1,50)
win = False
loss = False
play = True
Tries = 5
while play == True:
  print()
  guess = int(input("what's ur number guess?(0-50): "))
  if guess < secret:
    print("too smol")
    Tries -= 1
  if guess > secret:
    print("too big")
    Tries -= 1
  if guess == secret:
    print("GG")
    play = False
if Tries == 0:
  print("you lost, too many tries use lol...")