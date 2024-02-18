from oscusb3 import *

import numpy as np
import matplotlib.pyplot as plt

import csv

#Kanal sa koga se citaju podaci

def getsamples(self, ch, start = 1, stop = 10000):
        #
        x = self.getwfm(ch, start, stop)
        s = self.ask('ch' + str(ch) + '?').split(';')
        probe = float(s[0])
        scale = float(s[2])
        position = float(s[3])
        return (x - position) * scale * probe


o = Oscilloscope()
data = o.getsamples(ch=2)
data2 = o.getsamples(ch=1)
print(data)

f = open('CH2csvData', 'w')
#writer = csv.writer(f)
for i in range (0, len(data)):
    #writer.writerow(data[i])
    #writer.writerow('\n')
    f.write(data[i].astype(str))
    f.write('\n')
f.close()

f = open('CH1csvData', 'w')
#writer = csv.writer(f)
for i in range (0, len(data2)):
    #writer.writerow(data[i])
    #writer.writerow('\n')
    f.write(data[i].astype(str))
    f.write('\n')
f.close()

def getpdf(self, filename = '', ts = True):
        #
        f = self.getbmpraw()
        #
        fn = fname(filename, ts)
        ff = open(fn + '.bmp', 'wb')
        ff.write(f)
        ff.close()
        #
        os.system('convert -quiet ' + fn + '.bmp ' + fn + '.pdf')
        os.remove(fn + '.bmp')
        #
        return
getpdf(o,'test')


plt.rcParams["figure.figsize"]=[7.5, 3.5]
plt.rcParams["figure.autolayout"] = True
plt.title("OSC data")
plt.plot(data)
plt.plot(data2)

plt.show()
