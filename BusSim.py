import random
import time
from turtle import *
import os, sys
import webbrowser
from plyer import notification

USER = os.environ.get('USER')
if sys.platform == 'linux':
        sys.path.append(os.path.abspath(os.path.join('/home/%s'% (USER), 'Bussim')))
elif sys.platform == 'win32':
        sys.path.append(os.path.abspath(os.path.join('C://Users/%s'%(USER), 'Bussim-main')))
else:
        print('Your current OS: %s is not supported.'% (sys.platform))
        

try:
        import game
except ModuleNotFoundError:
        print('Game failed to import. Please reinstall from Github.')
        notification.notify(
            title = "BusSim - Error",
            message = "File game.py failed to load. Plese check installation.",
            timeout = 30,
            app_icon = "c://Users/Oliver/Bussim-compatibility/Error Popup.ico")
        webbrowser.open('https://github.com/ReviloWillson/Bussim.git', new = 2, autoraise=True)
        quit()
        


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
