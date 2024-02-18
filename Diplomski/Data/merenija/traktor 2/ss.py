from oscusb3 import *

import numpy as np
import matplotlib.pyplot as plt

import csv

#Kanal sa koga se citaju podaci
channel = 2

def getsamples(self, ch, start = 1, stop = 10000):
        #
        x = self.getwfm(ch, start, stop)
        s = self.ask('ch' + str(ch) + '?').split(';')
        probe = float(s[0])
        scale = float(s[2])
        position = float(s[3])
        return (x - position) * scale * probe

o = Oscilloscope()
data = o.getsamples(ch=channel)
print(data)

f = open('csvData', 'w')
#writer = csv.writer(f)
for i in range (0, len(data)):
    #writer.writerow(data[i])
    #writer.writerow('\n')
    f.write(data[i].astype(str))
    f.write('\n')
f.close()


plt.rcParams["figure.figsize"]=[7.5, 3.5]
plt.rcParams["figure.autolayout"] = True
plt.title("OSC data")
plt.plot(data)

plt.show()
