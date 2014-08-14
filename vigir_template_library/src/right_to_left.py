#! /usr/bin/env python

from sys import argv
import math
import numpy as np

def negateFloatInString(arg):
    newVal = float(arg)
    newVal = -newVal
    return str(newVal)

def quaternionFromFileValues(qwStr, qxStr, qyStr, qzStr):
    quat = np.zeros((4, ), dtype=np.float64)
    quat[0] = float(qwStr)
    quat[1] = float(qxStr)
    quat[2] = float(qyStr)
    quat[3] = float(qzStr)
    return quat

def quaternion_about_axis(angle, axis):
    """Return quaternion for rotation about axis.

    >>> q = quaternion_about_axis(0.123, [1, 0, 0])
    >>> numpy.allclose(q, [0.99810947, 0.06146124, 0, 0])
    True

    """
    q = np.array([0.0, axis[0], axis[1], axis[2]])
    qlen = np.linalg.norm(q)
    if qlen > np.finfo(float).eps:
        q *= math.sin(angle/2.0) / qlen
    q[0] = math.cos(angle/2.0)
    return q

def quaternion_multiply(quaternion1, quaternion0):
    """Return multiplication of two quaternions.

    >>> q = quaternion_multiply([1, -2, 3, 4], [-5, 6, 7, 8])
    >>> numpy.allclose(q, [-44, -14, 48, 28])
    True
    """
    w0, x0, y0, z0 = quaternion0
    w1, x1, y1, z1 = quaternion1
    return np.array((
        -x1*x0 - y1*y0 - z1*z0 + w1*w0,
         x1*w0 + y1*z0 - z1*y0 + w1*x0,
        -x1*z0 + y1*w0 + z1*x0 + w1*y0,
         x1*y0 - y1*x0 + z1*w0 + w1*z0  ), dtype=np.float64)



print " Program to convert Florian right hand grasps to left hand grasps"
print "    using y-axis reflection and -90 z-axis rotation"
print " Requires https://github.com/martinling/numpy_quaternion"

script, oldFile = argv

print " Source file: ", oldFile

zaxis = (0,0,1)

oldFilenameList = oldFile.split('.')
newFile = oldFilenameList[0]+"_left_modified.grasp"

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

            #change hand
            newList[0] = "{0: 5d}".format(int(newList[0]) + 1000)
            newList[1] = "{0: 3d}".format(int(newList[1]))
            newList[2] = 'left '
            #negate X values, 18 for final pose x value, 26 for pre-grasp pose x value
            newList[18] = negateFloatInString(newList[18])
            newList[26] = negateFloatInString(newList[26])
            #transform quaternions negate W and X to mirror plane YZ
            newList[21] = negateFloatInString(newList[21])
            newList[22] = negateFloatInString(newList[22])


            newList[29] = negateFloatInString(newList[29])
            newList[30] = negateFloatInString(newList[30])

            for item in newList[0:-1]:
                newFileptr.write(item+',')
            newFileptr.write('\n');
        else:
            break
else:
    print "File format is not as expected"



