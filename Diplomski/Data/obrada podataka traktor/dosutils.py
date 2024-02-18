import numpy as np
import matplotlib.pyplot as plt
from  matplotlib import patches

def zplane(b, a, ax = None):
    """Plot the complex z-plane given a transfer function.
    """

    # get a figure/plot
    if ax == None:
        w, h = plt.figaspect(1)
        fig, ax = plt.subplots(1, figsize=(w, h))
        plt.subplots_adjust(left = 0.2, bottom = 0.2)

    # create the unit circle
    uc = patches.Circle((0,0), radius=1, fill=False, color='black', ls='dashed')
    ax.add_patch(uc)
        
    # Get the poles and zeros
    p = np.roots(a)
    z = np.roots(b)
    k = b[0]/a[0]
    
    ## Count same poles/zeros
    # Make poles and zeros dictionaries
    poleCounts = {}
    for i in range(len(p)):
        if p[i].imag < 0:
            key = f'%f-%fj' % (p[i].real, -p[i].imag)
        else:
            key = f'%f+%fj' % (p[i].real, p[i].imag)
        if key in poleCounts:
            poleCounts[key] += 1
        else:
            poleCounts[key] = 1
    zeroCounts = {}
    
    for i in range(len(z)):
        if z[i].imag < 0:
            key = f'%f-%fj' % (z[i].real, -z[i].imag)
        else:
            key = f'%f+%fj' % (z[i].real, z[i].imag)
        if key in zeroCounts:
            zeroCounts[key] += 1
        else:
            zeroCounts[key] = 1
    
    # Plot the poles and set marker properties
    poleKeys = list(poleCounts.keys())
    for i in range(len(poleKeys)):
        pole = complex(poleKeys[i])
        ti = plt.plot(pole.real, pole.imag, 'rx', ms=10)
        plt.setp( ti, markersize=10.0, markeredgewidth=3.0, markeredgecolor='r', markerfacecolor='r')
        # place number of the same poles near the marker
        if poleCounts[poleKeys[i]] > 1:
            textstr = f'%d' % (poleCounts[poleKeys[i]])
            ax.text(pole.real+0.05, pole.imag+0.05, textstr, color='r')

    # Plot the zeros and set marker properties
    zeroKeys = list(zeroCounts.keys())
    for i in range(len(zeroKeys)):
        zero = complex(zeroKeys[i])
        t2 = plt.plot(zero.real, zero.imag, 'go', ms=10)
        plt.setp( t2, markersize=12.0, markeredgewidth=3.0, markeredgecolor='g', markerfacecolor='None')
        # place number of the same zeros near the marker
        if zeroCounts[zeroKeys[i]] > 1:
            textstr = f'%d' % (zeroCounts[zeroKeys[i]])
            ax.text(zero.real+0.05, zero.imag+0.05, textstr, color='g')
    allVals = np.concatenate((abs(p.real), abs(p.imag), abs(z.real), abs(z.imag)));
    limVal = max(allVals)*1.1
    if limVal < 1.1:
        limVal = 1.1
    
    ax.plot([-limVal, limVal], [0, 0], 'k--')
    ax.plot([0, 0], [-limVal, limVal], 'k--')
    
    ax.set_xlim([-limVal, limVal])
    ax.set_ylim([-limVal, limVal])
    
    ax.set_xlabel('Real')
    ax.set_ylabel('Imaginary')
    
    return z, p, k, ax