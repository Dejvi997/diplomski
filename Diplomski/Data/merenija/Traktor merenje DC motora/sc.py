from oscusb3 import *
o = Oscilloscope()
for i in range(0, 100):
    o.write('COUNTERFreq:CH2Value?')
    #o.waituntilready()
    data = 1/o.getvalue()
    print(data)
