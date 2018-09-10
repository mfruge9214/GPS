# Code created for CU Electric Car Project by Mike Fruge, Summer 2018

# Need to read in GPS data from GPSInfo program

import serial
def numtoword(array):
    x=len(array)
    word: List[str]=[]
    for i in range(0,x):
        element= chr(array[i])
        word.append(element)
    i=0
    return word

try:
    ser = serial.Serial(    #Info about the port used
    port= 'COM5',
    baudrate=4800,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=None)
except IOError:
    print('Unplug the GPS')
    ser = None
identifier=71                                       # 71 is ASCII for G
outside=[]
inside=[]
parse=0
entry=0
letter=0
j=0

# for i in range(0,3):
#     outside.append(inside)
# print(outside)

while ser:                                              #Parse Data loop
    data = ser.readline()
    if identifier == data[4]:
        print(data)
        while parse<len(data):
            if data[parse] == 44:
                outside.append(inside)
                parse +=1
                inside = []
                print('Inside Reset')
            elif data[parse] == 10:
                parse = 0
                inside = []
                print('Inside Reset')
                print('Outside = ', outside)
                break
            else:
                inside.append(data[parse])
                parse +=1
                print('inside =', inside)
        lat= numtoword(outside[2])
        print('Lat= ', lat)
        latdir= numtoword(outside[3])
        print('N or S= ', latdir)
        lng= numtoword(outside[4])
        print('Lng= ', lng)
        lngdir= numtoword(lng)
        print('E or W= ', lngdir)
        outside = []
        print('Outside Reset')

# Reset the parse counter, continue reading additional entries from the file
