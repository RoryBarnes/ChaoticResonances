import numpy as np
import matplotlib.pyplot as plt
import sys
import string
import subprocess as subp
try:
    import vplot
except:
    print('Cannot import vplot. Please install vplot.')

# Check correct number of arguments
if (len(sys.argv) != 2):
    print('ERROR: Incorrect number of arguments.')
    print('Usage: '+sys.argv[0]+' <pdf | png>')
    exit(1)
if (sys.argv[1] != 'pdf' and sys.argv[1] != 'png'):
    print('ERROR: Unknown file format: '+sys.argv[1])
    print('Options are: pdf, png')
    exit(1)

nlines=10001
t=[0 for j in range(nlines)]
earth_a_co=[0 for j in range(nlines)] # Coplanar, Earth, semi
earth_e_co=[0 for j in range(nlines)] # Coplanar, Earth, ecc
earth_i_co=[0 for j in range(nlines)] # Coplanar, Earth, incl
earth_p_co=[0 for j in range(nlines)] # Coplanar, Earth, long. of peri
earth_n_co=[0 for j in range(nlines)] # Coplanar, Earth, long. of asc. node
earth_l_co=[0 for j in range(nlines)] # Coplanar, Earth, mean longitude

outer_a_co=[0 for j in range(nlines)]
outer_e_co=[0 for j in range(nlines)]
outer_i_co=[0 for j in range(nlines)]
outer_p_co=[0 for j in range(nlines)]
outer_n_co=[0 for j in range(nlines)]
outer_l_co=[0 for j in range(nlines)]

earth_a_inc=[0 for j in range(nlines)] # Inclined, Earth, semi
earth_e_inc=[0 for j in range(nlines)] # Inclined, Earth, ecc
earth_i_inc=[0 for j in range(nlines)] # Inclined, Earth, incl
earth_p_inc=[0 for j in range(nlines)] # Inclined, Earth, long. of peri
earth_n_inc=[0 for j in range(nlines)] # Inclined, Earth, long. of asc. node
earth_l_co=[0 for j in range(nlines)] # Inclined, Earth, mean longitude

outer_a_inc=[0 for j in range(nlines)]
outer_e_inc=[0 for j in range(nlines)]
outer_i_inc=[0 for j in range(nlines)]
outer_p_inc=[0 for j in range(nlines)]
outer_n_inc=[0 for j in range(nlines)]
outer_l_inc=[0 for j in range(nlines)]

jtot_co=[0 for j in range(nlines)] # Total angular momentum, coplanar
etot_co=[0 for j in range(nlines)] # Total energy, coplanr

jtot_inc=[0 for j in range(nlines)] # Total angular momentum, inclined
etot_inc=[0 for j in range(nlines)] # Total energy, inclined


starco=open('coplanar/ChaosRes.star.forward')
earthco=open('coplanar/ChaosRes.earth.forward')
nepco=open('coplanar/ChaosRes.outer.forward')

starinc=open('inclined/ChaosRes.star.forward')
earthinc=open('inclined/ChaosRes.earth.forward')
nepinc=open('inclined/ChaosRes.outer.forward')

for line in starco:
    words=str.split(line)
    t[j]=float(words[0])
    jtot_co[j]=float(words[2])
    etot_co[j]=float(words[3])

for line in earthco:
    words=str.split(line)
    earth_a_co[j]=float(words[2])
    earth_e_co[j]=float(words[3])
    earth_i_co[j]=float(words[4])
    earth_p_co[j]=float(words[5])
    earth_n_co[j]=float(words[6])
    earth_l_co[j]=float(words[7])
    earth_instell_co[j]=float(words[8])

for line in outerco:
    words=str.split(line)
    outer_a_co[j]=float(words[2])
    outer_e_co[j]=float(words[3])
    outer_i_co[j]=float(words[4])
    outer_p_co[j]=float(words[5])
    outer_n_co[j]=float(words[6])
    outer_l_co[j]=float(words[7])

print('Read coplanar.')

for line in starinc:
    words=str.split(line)
    jtot_inc[j]=float(words[2])
    etot_inc[j]=float(words[3])

for line in earthinc:
    words=str.split(line)
    earth_a_inc[j]=float(words[2])
    earth_e_inc[j]=float(words[3])
    earth_i_inc[j]=float(words[4])
    earth_p_inc[j]=float(words[5])
    earth_n_inc[j]=float(words[6])
    earth_l_inc[j]=float(words[7])
    earth_instell_inc[j]=float(words[8])

for line in outerinc:
    words=str.split(line)
    outer_a_inc[j]=float(words[2])
    outer_e_inc[j]=float(words[3])
    outer_i_inc[j]=float(words[4])
    outer_p_inc[j]=float(words[5])
    outer_n_inc[j]=float(words[6])
    outer_l_inc[j]=float(words[7])

print('Read inclined.')

# First is coplanar
f, ax = plt.subplots(3,2,figsize=(6.5,9))

# Semi-major axis
plt.subplot(1,1,1)
earth_a_co=(earth_a_co/earth_a_co[0]-1)
plt.plot(Time,earth_a_co)
outer_a_co=(outer_a_co/outer_a_co[0]-1)
plt.plot(Time,outer_a_co,'-')
plt.ylabel(r'$(\Delta a / a - 1)$', fontsize=16)

# Eccentricity
plt.subplot(2,1,2)
plt.plot(Time,earth_e_co)
plt.plot(Time,outer_e_co,'-')
plt.xlabel('Time (yr)', fontsize=16)
plt.ylabel('Eccentricity', fontsize=16)

# Inclination
plt.subplot(1,2,2)
plt.plot(Time,earth_i_co)
plt.plot(Time,outer_i_co,'-')
plt.xlabel('Time (yr)', fontsize=16)
plt.ylabel(r'Inclination ($^\circ$)', fontsize=16)

# Conjunction Longitude
plt.subplot(2,2,2)
plt.plot(Time,(3*outer_l_co - earth_l_co))
plt.xlabel('Time (yr)', fontsize=16)
plt.ylabel(r'Conjunction Long.) ($^\circ$)', fontsize=16)

# Resonant Argument
plt.subplot(3,1,2)
plt.plot(Time,(3*outer_l_co - earth_l_co - 2*earth_p_co))
plt.plot(Time,(3*outer_l_co - earth_l_co - 2*outer_p_co),'r')
plt.xlabel('Time (yr)', fontsize=16)
plt.ylabel(r'Res. Arg.) ($^\circ$)', fontsize=16)

# Instellation
plt.subplot(3,2,2)
plt.plot(Time,earth_instell_co)
plt.xlabel('Time (yr)', fontsize=16)
plt.ylabel(r'Instellation (W/m$^2$)', fontsize=16)

if (sys.argv[1] == 'pdf'):
    plt.savefig('ChaosResCoplanar.pdf')
if (sys.argv[1] == 'png'):
    plt.savefig('ChaosResCoplanar.png')


# Next is inclined
f, ax = plt.subplots(3,2,figsize=(6.5,9))

# Semi-major axis
plt.subplot(1,1,1)
earth_a_inc=(earth_a_inc/earth_a_inc[0]-1)
plt.plot(Time,earth_a_inc)
outer_a_inc=(outer_a_inc/outer_a_inc[0]-1)
plt.plot(Time,outer_a_inc,'-')
plt.ylabel(r'$(\Delta a / a - 1)$', fontsize=16)

# Eccentricity
plt.subplot(2,1,2)
plt.plot(Time,earth_e_inc)
plt.plot(Time,outer_e_inc,'-')
plt.xlabel('Time (yr)', fontsize=16)
plt.ylabel('Eccentricity', fontsize=16)

# Inclination
plt.subplot(1,2,2)
plt.plot(Time,earth_i_inc)
plt.plot(Time,outer_i_inc,'-')
plt.xlabel('Time (yr)', fontsize=16)
plt.ylabel(r'Inclination ($^\circ$)', fontsize=16)

# Conjunction Longitude
plt.subplot(2,2,2)
plt.plot(Time,(3*outer_l_inc - earth_l_inc))
plt.xlabel('Time (yr)', fontsize=16)
plt.ylabel(r'Conjunction Long.) ($^\circ$)', fontsize=16)

# Resonant Argument
plt.subplot(3,1,2)
plt.plot(Time,(3*outer_l_inc - earth_l_inc - 2*earth_p_inc))
plt.plot(Time,(3*outer_l_inc - earth_l_inc - 2*outer_p_inc),'r')
plt.xlabel('Time (yr)', fontsize=16)
plt.ylabel(r'Res. Arg.) ($^\circ$)', fontsize=16)

# Instellation
plt.subplot(3,2,2)
plt.plot(Time,earth_instell_inc)
plt.xlabel('Time (yr)', fontsize=16)
plt.ylabel(r'Instellation (W/m$^2$)', fontsize=16)

if (sys.argv[1] == 'pdf'):
    plt.savefig('ChaosResInclined.pdf')
if (sys.argv[1] == 'png'):
    plt.savefig('ChaosResInclined.png')


# Finally the conservation plot
f, ax = plt.subplots(2,1,figsize=(6.5,9))

# Angular Momentum
plt.subplot(1,1,1)
DeltaAngMom_co=(jtot_co/jtot_co[0]-1)
plt.plot(Time,DeltaAngMom_co*1e9)
DeltaAngMom_inc=(jtot_inc/jtot_inc[0]-1)
plt.plot(Time,DeltaAngMom_inc*1e9,'-')
plt.ylabel(r'$(\Delta J / J - 1)/10^{9}$', fontsize=16)

#Now for energy
plt.subplot(2,1,2)
DeltaEnergy_co = (etot_co/etot_co[0]-1)
plt.plot(Time,DeltaEnergy_co*1e9)
DeltaEnergy_inc = (etot_inc/etot_inc[0]-1)
plt.plot(Time,DeltaEnergy_inc*1e9,'-')
plt.xlabel('Time (yr)', fontsize=16)
plt.ylabel(r'$(\Delta E / E - 1)/10^{9}$', fontsize=16)

if (sys.argv[1] == 'pdf'):
    plt.savefig('Conservation.pdf')
if (sys.argv[1] == 'png'):
    plt.savefig('Conservation.png')
