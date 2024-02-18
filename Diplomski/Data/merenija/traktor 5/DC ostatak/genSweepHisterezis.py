#! /usr/bin/python



__author__ = 'Predrag Pejovic'
__license__ = 'GPLv3'
__date__ = '2017-11-12'



from pylab import *
from oscusb3 import *
import sys
import csv

#
close('all')
rc('text', usetex = True)
rc('font', family = 'serif')
rc('font', size = 12)
rcParams['text.latex.preamble']=[r'\usepackage{amsmath}']
#

filename = 'test.pdf' #sys.argv[1] + '_' + timestamp() + '.pdf'

tsleep = .5

################################################################################
#
# generator
#
gen = usbtmc.Instrument(0x0957, 0x0407)
gen.write('output off')
gen.write('function dc')
#gen.write('voltage:amplitude 5')
gen.write('voltage:offset 0')
##gen.write('output:load 9.9e37')
##gen.write('output:load 50')
#gen.write('frequency 100')
gen.write('output on')
#
    
def genfreq(offset):
	gen.write('voltage:offset ' + str(offset))
#
################################################################################


ch1scale = '2'
ch2scale = '2'
tscale = '1e-3'

################################################################################
#
o = Oscilloscope(shy = True)
#
o.write('*rst')
#
o.write('select:ch1 on')
o.write('ch1:probe 10')
o.write('ch1:scale ' + ch1scale)
#o.write('ch1:coupling ac')
#o.write('ch1:bandwidth on')
#
o.write('select:ch2 on')
o.write('ch2:probe 10')
o.write('ch2:scale ' + ch2scale)
#o.write('ch2:coupling dc')
#o.write('ch2:bandwidth on')
#
o.write('horizontal:scale ' + str(tscale))
o.write('horizontal:position 0')
#
o.write('trigger:main:edge:source ext')
o.write('trigger:main:level 0.7')
#
o.waituntilready()
#
################################################################################


MEAN_vec = np.array([])
MEAN_vec2 = np.array([])
AMP_vec = np.array([])
offset = np.array([])

#for frequency in linspace(140, 2000, 200):
for amplitude in linspace(0, 4.6, 200):

	genfreq(amplitude)
	
	time.sleep(tsleep)
	
	o.write("measure:immed:source ch2; type amplitude");
	amp2 = float( o.ask("measure:immed:value?") );
	
	o.write("measure:immed:source ch2; type mean");
	mean2 = float (  o.ask("measure:immed:value?") );
	
	AMP = amp2
	MEAN = mean2
	
	AMP_vec = append(AMP_vec, AMP)
	MEAN_vec = append(MEAN_vec, MEAN)
	
	offset = append(offset, amplitude)
	
	print(AMP, MEAN)

#Cuvanje u csv fajl	
f = open('meanData', 'w')
for i in range (0, len(MEAN_vec)):
	f.write(MEAN_vec[i].astype(str))
	f.write('\n')
f.close()
	
f = open('AmpData', 'w')
for i in range (0, len(offset)):
	f.write(offset[i].astype(str))
	f.write('\n')
f.close()


for amplitude in linspace(4.6, 0, 200):

	genfreq(amplitude)
	
	time.sleep(tsleep)
	
	o.write("measure:immed:source ch2; type amplitude");
	amp2 = float( o.ask("measure:immed:value?") );
	
	o.write("measure:immed:source ch2; type mean");
	mean2 = float (  o.ask("measure:immed:value?") );
	
	AMP = amp2
	MEAN = mean2
	
	AMP_vec = append(AMP_vec, AMP)
	MEAN_vec2 = append(MEAN_vec2, MEAN)
	
	offset = append(offset, amplitude)
	
	print(AMP, MEAN)
	
#Cuvanje u csv fajl	
f = open('meanDataNazad', 'w')
for i in range (0, len(MEAN_vec2)):
	f.write(MEAN_vec2[i].astype(str))
	f.write('\n')
f.close()

gen.write('output off')

figure(1)
#
offset = np.linspace(0, 4.6, 200)
plot(offset, MEAN_vec, 'b')
offset = np.linspace(4.6, 0, 200)
plot(offset, MEAN_vec2, 'r')
grid()
#
xlabel(r'$v \, [\text{V}]$')
ylabel(r'$mean [V]$')
title(u'Prenosna karakteristika sistema')
#
savefig(filename)
show()
