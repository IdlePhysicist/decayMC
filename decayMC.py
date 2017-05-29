#
#   DEACY MONTE CARLO METHOD VERSION II
#   Eoghan Conlon O'Neill 2016
#
from random import random
from numpy import arange, loadtxt
from pylab import *
import os
from astropy.table import Table
from astropy.io import ascii

#   Constants
parentPopulation = int(input('Enter initial number of atoms: '))
daughter1Population = 0
daughter2Population = 0
daughter3Population = 0
daughter4Population = 0
daughter5Population = 0
halfLife = loadtxt("U238_chain.txt", usecols=(1,))
dt = float(input('Enter time step (s): '))
probDecay1 = 1 - 2**(-dt/halfLife[8])   # Probability of decay in one step
probDecay2 = 1 - 2**(-dt/halfLife[8])
probDecay3 = 1 - 2**(-dt/halfLife[9])
probDecay4 = 1 - 2**(-dt/halfLife[11])
probDecay5 = 1 - 2**(-dt/halfLife[11])
tmax = float(input('Enter simulation time (s): '))

#   Lists of plot points
tPoints = arange(0.0,tmax,dt)
parentPoints = []
daughter1Points = []
daughter2Points = []
daughter3Points = []
daughter4Points = []
daughter5Points = []

#   Main loop
for t in tPoints:
    parentPoints.append(parentPopulation)
    daughter1Points.append(daughter1Population)
    daughter2Points.append(daughter2Population)
    daughter3Points.append(daughter3Population)
    daughter4Points.append(daughter4Population)
    daughter5Points.append(daughter5Population)
    
    # Calculate the number of atoms that decay
    decay1 = 0
    decay2 = 0
    decay3 = 0
    decay4 = 0
    decay5 = 0
    for i in range(parentPopulation):
        if random()<probDecay1:
            decay1 += 1
    for i in range(daughter1Population):
        if random()<probDecay2:
            decay2 += 1
    for i in range(daughter2Population):
        if random()<probDecay3:
            decay3 += 1
    for i in range(daughter3Population):
        if random()<probDecay4:
            decay4 += 1
    for i in range(daughter4Population):
        if random()<probDecay5:
            decay5 += 1
    parentPopulation -= decay1
    daughter1Population += (decay1 - decay2)
    daughter2Population += (decay2 - decay3)
    daughter3Population += (decay3 - decay4)
    daughter4Population += (decay4 - decay5)
    daughter5Population += decay5

#   Generating the output file
output = Table([tPoints, parentPoints, daughter1Points, daughter2Points, daughter3Points, daughter4Points, daughter5Points], names=['Time','Parent Pop.','First Daughter Pop.','Sec. Daughter Pop.','3rd Daughter Pop.', '4th Daughter', '5th Dau'])
#os.system("touch decayP.txt")
ascii.write(output, 'decayP.txt', overwrite=True)

#   Plotting
figure(figsize=(12,8))
rc('font', family='sans')
rc('xtick', labelsize='small')
rc('ytick', labelsize='small')

plot(tPoints, parentPoints, color='Blue', label='Parent')
plot(tPoints, daughter1Points, color='Red', label='Daughter 1')
plot(tPoints, daughter2Points, color='Green', label='Daughter 2')
plot(tPoints, daughter3Points, color='Black', label='Daughter 3')
plot(tPoints, daughter4Points, color='Blue', label='Daughter 4')

print halfLife[8]/log(2)

#ylim(0,100)
#yscale('log')
#xscale('log')
xlabel("Elapsed Time (s)")
ylabel("Population")
legend(loc='upper right')
savefig("Sim Plot.png")
#show() # Uncomment this to see the plot as it's drawn
