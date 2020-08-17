import numpy as np
from numpy.random import randint

print('Welcome to flip a coin!')
bet = str(input('Hedge your bets: '))
if bet == 'Heads' or bet == 'Tails':
  print('Flipping now...')
else: 
  while bet != 'Heads' and bet != 'Tails':
    print('Invalid input! Must be Heads or Tails. Please try again.')
    bet = str(input('Hedge your bets: '))
  print('Flipping now...')
rand = randint(0, 2)
if rand == 1:
  if bet == 'Heads':
    print('It was heads! You were correct!')
  elif bet == 'Tails':
    print('It was heads! You were incorrect.')
if rand == 0:
  if bet == 'Tails':
    print('It was tails! You were correct!')
  elif bet == 'Heads':
    print('It was tails! You were incorrect.')

# STOP COUNTING CHARACTERS
x = """import numpy as np
from numpy.random import randint

print('Welcome to flip a coin!')
bet = str(input('Hedge your bets: '))
if bet == 'Heads' or bet == 'Tails':
  print('Flipping now...')
else: 
  while bet != 'Heads' and bet != 'Tails':
    print('Invalid input! Must be Heads or Tails. Please try again.')
    bet = str(input('Hedge your bets: '))
  print('Flipping now...')
rand = randint(0, 2)
if rand == 1:
  if bet == 'Heads':
    print('It was heads! You were correct!')
  elif bet == 'Tails':
    print('It was heads! You were incorrect.')
if rand == 0:
  if bet == 'Tails':
    print('It was tails! You were correct!')
  elif bet == 'Heads':
    print('It was tails! You were incorrect.')"""
print("Your number of characters is: {}".format(len(x)))
print("Your number of lines is: {}".format(x.count('\n')))