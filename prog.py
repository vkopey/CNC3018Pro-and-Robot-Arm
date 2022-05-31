# -*- coding: utf-8 -*-
"Програма для керування/програмування робота 4DOF ARM acrylic robot arm https://www.sinoning.com/docs/4dofarm/"
#import sys
#sys.path.append(r"d:\Python\robotArm")
from pyfirmata import Arduino, util

time=util.time
board = Arduino('COM15', baudrate=57600)
s1=board.get_pin('d:3:s')
s1.write(90)
s2=board.get_pin('d:5:s')
s2.write(50)
s3=board.get_pin('d:6:s')
s3.write(90)
s4=board.get_pin('d:9:s')
s4.write(150)

def key_handler(event=None):
    if event:
        k=event.keycode
        print "keycode=",k
        if   k==39: s=s1; st=-1 # <вправо>
        elif k==37: s=s1; st=1 # <вліво>
        elif k==40: s=s2; st=-1 # <вниз>
        elif k==38: s=s2; st=1 # <вверх>
        elif k==34: s=s3; st=-1 # назад <PageDown>
        elif k==33: s=s3; st=1 # вперед <PageUp>
        elif k==36: s=s4; st=-1 # закрити <Home>
        elif k==35: s=s4; st=1 # відкрити <End>
        elif k==27: print P; board.exit(); r.destroy(); return P # вихід <Esc>
        elif k==80: return addPoint()  # додати точку <P>
        else: s=None
        if s:
            s.write(s.value+st)
            time.sleep(0.1)
            print s.value

P=[] # опорні точки
def addPoint():
    p=s1.value, s2.value, s3.value, s4.value
    P.append(p)
    print p
    return p

if __name__=="__main__":
    import Tkinter as tk
    r = tk.Tk()
    r.bind('<Key>', key_handler)
    r.mainloop()
