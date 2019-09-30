#!/usr/bin/env python

'readTextFile.py -- read and display test file'

# get filename
fname = input('Enter file name: ')

# attempt to open file or reading
try:
    fobj = open(fname, 'r')
except IOError as e:
    print("*** file open error:", e)
else:
    # display contents to the screen
    for eachLine in fobj:
        print(eachLine, end=' ')
    fobj.close()