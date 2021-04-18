#
# Coin Flip Streaks
import random

numberOfStreaks = 0
lst = []
streak = 0
for experimentNumber in range(10000):
	# Code that creates a list of 100 'heads' or 'tails' values.
	for i in range(100):
		lst.append(random.randint(0, 1))

	# Code that checks if there is a streak of 6 heads or tails in a row.
	for index, side in enumerate(lst):
		if side == 0:
			pass
		elif index == index - 1:
			streak += 1
			
		if streak == 6:
			numberOfStreaks += 1

print('Chance of streak: %s%%' % (numberOfStreaks / 100))
