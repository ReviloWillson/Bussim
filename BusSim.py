import random
import time
from turtle import *
import os, sys

USER = os.environ.get('USER')

sys.path.append(os.path.abspath(os.path.join('/home/%s' % (USER), 'bussim')))

import game



print('[  %s  ]: Loading Launcher...' % (USER))

title('BusSim - Loading')

hideturtle()

for num in range(3):
	for num in range(360):
		try:
			forward(1)
			right(1)
		except Terminator:
			print('Exited')
			quit()
		#end try
	#End For
	right(90)
	forward(10)
	left(90)
	if num == 1:
		color('red')
	else:
		color('blue')
#End For
bye()

print('[  %s  ]: Loding complete.' % (USER))

print('BusSim\nCopyright(C) CJO Games 2022')

launcher = input('Type [\'launch\'] to open BusSim or [\'quit\'] to exit launcher.\n')

launcher = launcher.lower()

if launcher == 'launch':
	game.run()
else:
	print('Exited')
