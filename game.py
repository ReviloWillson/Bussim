import random, sys, os


USER = os.environ.get('USER')

if sys.platform == 'linux':
	sys.path.append(os.path.abspath(os.path.join('/home/%s'% (USER), 'Bussim')))
elif sys.platform == 'win':
	sys.path.append(os.path.abspath(os.path.join('C://Users/%s'%(USER), 'Bussim')))
else:
	print('Your OS (%s) is not supported.'% (sys.platform))
	quit()
import vars






def b_Bus():
	money = vars.m_St
	b_down = input('Your Bus has broken down! Fix it for £3,000 or buy a new one for £400,000. (f/n)\n')
	if b_down == 'f':
		print('You fixed your bus')
		money -= 3000
		
		print('Money Remaining:£%s' % (money))
	else:
		print('You bought a new bus')
		money -= 400000
		print('Money Remaining:£%s' % (money))
	vars.m_St = money

def c_Bus():
	money = vars.m_St
	s_Lc = input('You have crashed your bus. A passenger has asked to view your License. Show it? (y/n)\n')
	if s_Lc == 'y':
		print('The passenger has seen your license and found it expired! You pay the fine of £500,000.')
		money -= 500000
		print('Remaining money:£%s' % (money))
		print('Game Over!\nReason: You were banned from driving!\nMoney:£%s' % (money))
		quit()
		
	else:
		print('You declined the passenger\'s request. you pay a fine of £900,000')
		money -=900000
		print('Remaining money:£%s' % (money))
	vars.m_St = money

def h_Dr():
	money = vars.m_St
	d_Hi = input('A driver has offered to work for you. Hire them for £20,000 or face a penalty fine. (h/n)\n')
	if d_Hi == 'h':
		print('You hired the driver.')
		money -= 20000
		print('Remaining money:£%s' % (money))
	else:
		print('You crashed a bus and payed £3000.')
		money -= 3000
		print('Remaining money:£%s' % (money))
	vars.m_St = money

def s_Ru():
	money = vars.m_St
	print('You made a sucessful run!')
	money += 20000
	print('Remaining money:£%s'  % (money))
	vars.m_St = money
	

def run():
	go = True
	while go:
		if vars.m_St > -100000:
			sel = random.randint(1, 4)
			if sel == 1:
				b_Bus()
			elif sel == 2:
				c_Bus()
			elif sel == 3:
				h_Dr()
			elif sel == 4:
				s_Ru()
		else:
			print('You have gone bankrupt!')
			quit()


