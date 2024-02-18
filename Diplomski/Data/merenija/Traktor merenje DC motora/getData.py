from oscusb3 import *

import csv


o = Oscilloscope()
#o.ask('ch2:frequency?')

f = open('csvData', 'w')

writer = csv.writer(f)

#data = o.getsamples()

o.write('COUNTERFreq:CH2Value?')
o.waituntilready()
data = o.getvalue()

writer.writerow(data)

f,close()


