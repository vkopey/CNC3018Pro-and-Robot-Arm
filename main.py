# -*- coding: utf-8 -*-
"Виконує програму для робота"

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

def move(s, y):
    x=s.value
    i=1 if x<y else -1
    while x!=y:
        s.write(x)
        time.sleep(0.1)
        x=x+i
"""
move(s1, 1)
move(s2, 45)
move(s2, 50)
move(s1, 90)
"""

def runProgram(program=[]):
    i=1
    for p1,p2,p3,p4 in program:
        print i, [p1,p2,p3,p4]
        move(s1, p1)
        move(s2, p2)
        move(s3, p3)
        move(s4, p4)
        i+=1

prog1=[(90, 64, 90, 150),(176, 64, 90, 150), (176, 64, 112, 150), (176, 64, 112, 80), (176, 79, 112, 80), (176, 79, 76, 80), (80, 79, 76, 80), (80, 79, 98, 80), (80, 67, 98, 80), (80, 67, 98, 149), (80, 67, 58, 149), (80, 67, 98, 149), (80, 67, 98, 80), (80, 78, 98, 80), (80, 78, 72, 80), (176, 78, 72, 80), (176, 78, 107, 80), (176, 65, 107, 80), (176, 65, 107, 157), (176, 65, 81, 157), (90, 50, 90, 150)]

import mysimple_stream
for i in range(1):
    runProgram(program=prog1[:11])
    mysimple_stream.run("grbl0.gcode")
    mysimple_stream.run()
    runProgram(program=prog1[11:])

board.exit()


