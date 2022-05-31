# -*- coding: utf-8 -*-
"Виконує програму для верстата"

import serial
import time

def run(file='grbl.gcode'):
    # Open grbl serial port
    s = serial.Serial('COM14',115200)

    # Open g-code file
    f = open(file,'r')

    # Wake up grbl
    s.write("\r\n\r\n")
    time.sleep(2)   # Wait for grbl to initialize
    s.flushInput()  # Flush startup text in serial input

    # Stream g-code to grbl
    for line in f:
        l = line.strip() # Strip all EOL characters for consistency
        print 'Sending: ' + l,
        s.write(l + '\n') # Send g-code block to grbl
        grbl_out = s.readline() # Wait for grbl response with carriage return
        print ' : ' + grbl_out.strip()

    # Close file and serial port
    f.close()
    s.close()