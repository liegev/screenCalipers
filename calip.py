import pyautogui, sys, math, os

state = 'a'
mode = 'f'
null = 1

## This is a comment - define your functions here....


def menu():
    print('|--- Screen calipers        version 4      ---|')
    print('|Home>                                        |')
    print('|                                             |')
    print('| type a LETTER and press ENTER               |')
    print('|                                             |')
    print('|  lc --- to enter origin with mouse  **      |')
    print('|  l  --- for absolute location               |')
    print('|  lo --- to enter offset manually            |')
    print('|  d  --- for distance       (not working)    |')
    print('|  q  --- to quit                             |')
    print('|                                             |')
    print('|                                             |')

def menu_l():
    print('|--- Screen calipers        version 4      ---|')
    print('|Home>absolute location mode                  |')
    print('|                                             |')
    print('| press ENTER to save location                |')
    print('|                                             |')
    print('| press CTRL+C to escape                      |')
    print('|                                             |')
    print('|                                             |')
    print('|                                             |')
    print('|                                             |')
    print('|                                             |')
    print('|                                             |')

def menu_lo():
    print('|--- Screen calipers        version 4      ---|')
    print('|Home>manual offset mode                      |')
    print('|                                             |')
    print('| press ENTER to save location                |')
    print('|                                             |')
    print('| press CTRL+C to escape                      |')
    print('|                                             |')
    print('|                                             |')
    print('|                                             |')
    print('|                                             |')
    print('|                                             |')
    print('|                                             |')

def menu_lc():
    print('|--- Screen calipers        version 4      ---|')
    print('|Home>set origin with mouse mode              |')
    print('|                                             |')
    print('| *press 0 and ENTER to set origin*           |')
    print('| press ENTER to save location                |')
    print('|                                             |')
    print('| press CTRL+C to escape                      |')
    print('|                                             |')
    print('|                                             |')
    print('|                                             |')
    print('|                                             |')
    print('|                                             |')
    print('|                                             |')

def menu_d():
    print('|--- Screen calipers        version 4      ---|')
    print('|Home>distance calculator                     |')
    print('|                                             |')
    print('| *hit ENTER at first location                |')
    print('| *hit ENTER at second location               |')
    print('|                                             |')
    print('| press CTRL+C to escape                      |')
    print('|                                             |')
    print('|                                             |')
    print('|                                             |')


def locate():
    while True:
        x1, y1 = pyautogui.position()
        positionStr = 'X: ' + str(x1).rjust(4) + ' Y: ' + str(y1).rjust(4) 
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)

def locate_off():
    offx = int(input('enter x offset...  '))
    offy = int(input('enter y offset...  '))
    while True:
        x1, y1 = pyautogui.position()
        positionStr = 'X: ' + str(x1-offx).rjust(4) + ' Y: ' + str(y1-offy).rjust(4)
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)

def locate_click():
    null = input()
    offx, offy = pyautogui.position()
    while True:
        x1, y1 = pyautogui.position()
        positionStr = 'X: ' + str(x1-offx).rjust(4) + ' Y: ' + str(y1-offy).rjust(4)
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)

def locate_distance():
    null = 'a'
    while null != 'q':
        print('|--- Screen calipers        version 4      ---|')
        print('|Home>distance calculator                     |')
        print('|                                             |')
        print('| *hit ENTER at first location                |')
        print('| *hit ENTER at second location               |')
        print('|                                             |')
        print('| press q and ENTER to escape                 |')
        print('|                                             |')
        print('|                                             |')
        print('|                                             |')
        null = input('|')
        xloc1, yloc1 = pyautogui.position()
        keyTrig2 = input('|')
        xloc2, yloc2 = pyautogui.position()
        xdist = xloc2-xloc1
        ydist = yloc2-yloc1
        ddist = math.ceil(math.sqrt((xdist^2)+(ydist^2)))
        print('|  The X distance is        = ' + str(xdist))
        print('|  The Y distance is        = ' + str(ydist))
        print('|  The diagonal distance is = ' + str(ddist))
        print('| press enter to measure again   ')
        null = input()
        os.system('clear')

## Make your nested fucntions here....

os.system('clear')
while state != 'q':
    menu()
    state = input('enter choice\n>>')
    try:
        if state == 'l':
            os.system('clear')
            menu_l()
            locate()
        if state == 'lo':
            os.system('clear')
            menu_lo()
            locate_off()
        if state == 'lc':
            os.system('clear')
            menu_lc()
            locate_click()
        if state == 'd':
            os.system('clear')
            locate_distance()
    except KeyboardInterrupt:
        os.system('clear')
os.system('clear')
print('Thank you for using this software - have a wonderful day.')