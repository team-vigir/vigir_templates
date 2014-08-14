#! /usr/bin/env python

from sys import argv
import math
import numpy as np



print " Program to convert Florian right hand grasps from GraspIt output in millimeters"
print "    to standard units in meters "

script, oldFile = argv

print " Source file: ", oldFile

zaxis = (0,0,1)

oldFilenameList = oldFile.split('.')
newFile = oldFilenameList[0]+"_meters.grasp"

print 'New file: %s' %newFile

newFileptr = open(newFile, 'w')
oldFileptr = open(oldFile, 'r')

line = oldFileptr.readline();
newList = []
if line[0] == '#':
    newFileptr.write(line)
    while True:
        line = oldFileptr.readline()
        if line != "":
            splitLine = line.split(',')
            newList= splitLine
            #print line
            #print "---------------------------------"
            #for item in newList:
            #            print item
            #print "------------------------------------"

            # Format ID values
            newList[0] = "{0: 5d}".format(int(newList[0]))
            newList[1] = "{0: 3d}".format(int(newList[1]))

            #Convert positions from millimeters to meters
            newList[18] = str(float(newList[18])*0.001)
            newList[19] = str(float(newList[19])*0.001)
            newList[20] = str(float(newList[20])*0.001)

            newList[26] = str(float(newList[26])*0.001)
            newList[27] = str(float(newList[27])*0.001)
            newList[28] = str(float(newList[28])*0.001)

            for item in newList[0:-1]:
                    newFileptr.write(item+',')
            newFileptr.write('\n');
        else:
            break
else:
    print "File format is not as expected"



