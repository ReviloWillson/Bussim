import random, sys, os, time


USER = os.environ.get('USER')

if sys.platform == 'linux':
        sys.path.append(os.path.abspath(os.path.join('/home/%s'% (USER), 'Bussim')))
elif sys.platform == 'win32':
        sys.path.append(os.path.abspath(os.path.join('C://Users/%s'%(USER), 'Bussim-main')))
else:
        print('Your OS (%s) is not supported.'% (sys.platform))
        
import vars






def b_Bus():
        money = vars.m_St
        print('-'*50)
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
        vars.points += 1
        lic = vars.has_License
        print('-'*50)
        print('You crashed your bus. A passenger has asked to see your license.')
        if lic:
                print('The passenger has seen your license. It is fine.\nMoney Remaining:£%s.'%(money))
                print('Points on license:%s'% (vars.points))
        else:
                print('You do not have a license!')
                print('Game over!\nYou were caught driving without a license.')
                time.sleep(3)
                quit()
        print('-'*50)
                
        

def h_Dr():
        money = vars.m_St
        print('-'*50)
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
        print('-'*50)
        money = vars.m_St
        print('You made a sucessful run!')
        money += 20000
        print('Remaining money:£%s'  % (money))
        vars.m_St = money

def Lc():
        print('-'*50)
        money = vars.m_St
        lic = vars.has_License
        if lic:
                pass
        elif not lic:
                b_l = input('Buy a license for 3,000 or continue without? (l/c)\n')
                if b_l == 'l':
                        lic = True
                        money -= 3000
                        print('You now have a license! Money remaining: £%s.'% (money))
                        vars.has_License = True
                        vars.m_St = money
                else:
                        print('You didn\'t buy a license. Be careful out there...:-)')
                        
        

def run():
        go = True
        while go:
                if vars.points > 8:
                        print('Your license was revoked.')
                        vars.has_License = False
                if vars.m_St > -100000:
                        sel = random.randint(1, 5)
                        if sel == 1:
                                b_Bus()
                        elif sel == 2:
                                c_Bus()
                        elif sel == 3:
                                h_Dr()
                        elif sel == 4:
                                s_Ru()
                        elif sel == 5:
                                Lc()
                else:
                        print('You have gone bankrupt!')
                        time.sleep(3)
                        quit()

                        

