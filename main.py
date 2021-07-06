import random
secret = random.randint(1,50)
win = False
loss = False
play = True
tries = 0
while play == True:
  print()
  guess = int(input("what's ur number guess?(0-50): "))
  if guess < secret:
    print("too smol")
    tries += 1
  if guess > secret:
    print("too big")
    tries += 1
  if guess == secret:
    print("GG")
    tries += 1
    print(f"You have finished in {tries} Tries... Good work!")