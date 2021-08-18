# -*- coding : UTF-8 -*-
import win32api
import win32con
import win32gui
import time
import datetime
from PIL import Image, ImageGrab

def get_wows():
    wowsw = u'Wargaming.net Game Center'
    handle = win32gui.FindWindow(0, wowsw)
    if handle == 0:
        print('none')
        return None
    else:
        return win32gui.GetWindowRect(handle)
def ax(x, screen):
    return (screen[2] - screen[0]) * x / 1100
def ay(y, screen):
    return (screen[3] - screen[1]) * y / 700
def get_hash(img):
    img = img.resize((16, 16), Image.ANTIALIAS).convert('L')
    avg = sum(list(img.getdata())) / 256
    s = ''.join(map(lambda i: '0' if i < avg else '1', img.getdata()))
    return ''.join(map(lambda j: '%x' % int(s[j:j+4], 2), range(0, 256, 4)))
def get_diff(hash1, hash2, n=20):
    diff = sum(ch1 != ch2 for ch1, ch2 in zip(hash1, hash2))
    b = False
    assert len(hash1) == len(hash2)
    if sum(ch1 != ch2 for ch1, ch2 in zip(hash1, hash2)) < n:
        b = True
    return b
def get_reso():
    global screen, topx, topy
    screen = get_wows()
    topx, topy = screen[0], screen[1]
def get_scr(a, b, c, d):
    img = ImageGrab.grab((topx + ax(a, screen), topy + ay(b, screen),
                                topx + ax(c, screen), topy + ay(d, screen)))
    hash = get_hash(img)
    return hash
def mouse(x, y):
    xt = int(topx + ax(x,screen))
    yt = int(topy + ay(y,screen))
    win32api.SetCursorPos((xt, yt))
    time.sleep(0.2)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, xt, yt, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, xt, yt, 0, 0)
    time.sleep(0.2)
def kbd(x):
    win32api.keybd_event(x,0,0,0)
    win32api.keybd_event(x,0,win32con.KEYEVENTF_KEYUP,0)
    time.sleep(0.1)

def quitbattle():
    kbd(27)
    time.sleep(1)
    mouse(100,100)
    mouse(644,312)
    time.sleep(1)
    mouse(575,445)
    time.sleep(5)

def copy_paste(chatcount):
    if chatcount == 1:
        kbd(13)#enter
        kbd(9)#tab
        win32api.keybd_event(17,0,0,0)
        win32api.keybd_event(86,0,0,0)
        win32api.keybd_event(86,0,win32con.KEYEVENTF_KEYUP,0)
        win32api.keybd_event(17,0,win32con.KEYEVENTF_KEYUP,0)
        kbd(13)
        return 0






if __name__ == '__main__':
    get_reso()
    get_scr(0,0,10,10)

    #get_scr(0,0,1296,759)
    #print(hash)
