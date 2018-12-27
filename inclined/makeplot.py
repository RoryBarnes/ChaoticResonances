import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import sys
try:
    import vplot as vpl
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

#Typical plot parameters that make for pretty plot
mpl.rcParams['figure.figsize'] = (10,8)
mpl.rcParams['font.size'] = 16.0

# Load data
output = vpl.GetOutput()

# Extract data
time = output.star.Time/1.0e6 # Scale to Myr
ecc1 = output.earth.Eccentricity
ecc2 = output.outer.Eccentricity
inc1 = output.earth.SpiNBodyInc
inc2 = output.outer.SpiNBodyInc
varpi1 = output.earth.LongP
varpi2 = output.outer.LongP
a1 = output.earth.SemiMajorAxis
a2 = output.outer.SemiMajorAxis
#instell = output.earth.Instellation
#mean1 = output.earth.MeanL
mean2 = output.outer.MeanLongitude

# Plot
fig, axes = plt.subplots(nrows=3, ncols=2, sharex=True)
color = "k"

## Upper left: a1 ##
axes[0,0].plot(time, a1)

# Format
axes[0,0].set_xlim(time.min(),time.max())
#axes[0,0].legend(loc="best")
axes[0,0].set_ylim(0.9*a1.min(),1.1*a1.min())
axes[0,0].set_ylabel("Semi-major Axis [AU]")

## Upper right: eccentricities ##
axes[0,1].plot(time, ecc1)
axes[0,1].plot(time, ecc2, color=vpl.colors.pale_blue)

# Format
axes[0,1].set_xlim(time.min(),time.max())
axes[0,1].set_ylim(0.0,1.1*ecc1.max())
axes[0,1].set_ylabel("Eccentricity")

## Middle left: inclination ##
axes[1,0].plot(time,inc1)
axes[1,0].plot(time,inc2,color=vpl.colors.pale_blue)

# Format
axes[1,0].set_xlim(time.min(),time.max())
axes[1,0].legend(loc="best")
axes[1,0].set_ylim(0,180)
axes[1,0].set_xlabel("Time [Myr]")
axes[1,0].set_ylabel(r"Inclination [^\circ]")

## Middle right: Resonant Argument ##
#arg1 = np.fabs(np.fmod(3*out.outer.MeanL - out.earth.MeanL - 2*out.earth.LongP, 360.0))
#arg2 = np.fabs(np.fmod(3*out.outer.MeanL - out.earth.MeanL - 2*out.outer.LongP, 360.0))

#axes[1,1].plot(Time,arg1)
#axes[1,1].plot(Time,arg2,color=vpl.pale_blue)

# Format
#axes[1,1].set_xlim(time.min(),time.max())
#axes[1,1].set_ylim(0, 360)
#axes[1,1].set_xlabel("Time [Myr]")
#axes[1,1].set_ylabel(r"Res. Arg. [$^{\circ}$]")

## Bottom Left: Conjunction Longitude ##
#conj = np.fabs(np.fmod(3*out.outer.MeanL - out.earth.MeanL, 360.0))

#axes[2,0].plot(Time,conj)

# Format
#axes[2,0].set_xlim(time.min(),time.max())
#axes[2,0].set_ylim(0, 360)
#axes[2,0].set_xlabel("Time [Myr]")
#axes[2,0].set_ylabel(r"Conj. Long. [$^{\circ}$]")

## Bottom Rightt: Instellation ##
axes[2,1].plot(time,output.earth.Instellation)

# Format
axes[2,0].set_xlim(time.min(),time.max())
axes[2,0].set_ylim(output.earth.Instellation.min(),output.earth.Instellation.max())
axes[2,0].set_xlabel("Time [Myr]")
axes[2,0].set_ylabel(r"Instellation [W/m$^2$]")

# Final formating
fig.tight_layout()
for ax in axes.flatten():
    # Rasterize
    ax.set_rasterization_zorder(0)

    # Set tick locations
    ax.set_xticklabels(["0", "2", "4", "6", "8", "10"])
    ax.set_xticks([0, 2, 4, 6, 8, 10])

if (sys.argv[1] == 'pdf'):
    fig.savefig('ChaosRes.pdf', bbox_inches="tight", dpi=600)
if (sys.argv[1] == 'png'):
    fig.savefig('ChaosRes.png', bbox_inches="tight", dpi=600)
