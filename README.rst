Chaotic Eccentricity-Inclination Resonances
============

Overview
--------

Orbital evolution of System U in `Barnes et al (2015) <http://adsabs.harvard.edu/abs/2015ApJ...801..101B>`_
(see Fig. 13) as predicted by `vplanet <https://github.com/VirtualPlanetaryLaboratory/vplanet>`_.

===================   ============
**Date**              12/20/18
**Author**            Rory Barnes
**Modules**           SpiNBody
**Approx. runtime**   14 hr
**Source code**       `vplanet <https://github.com/VirtualPlanetaryLaboratory/vplanet>`_,
                      `vplot <https://github.com/VirtualPlanetaryLaboratory/vplot>`_
===================   ============

To run this example
-------------------

.. code-block:: bash

  vplanet vpl.in
  python makeplot.py <pdf | png>


Expected output
---------------

.. figure:: ChaosRes.png
   :width: 600px
   :align: center

*Top Left:* The semi-major axis evolution of the inner (Earth-like) planet changes
by about 0.5% every 1000 years. (Note the x-axis scale is different for this panel.)
*Top Right:* The eccentricity evolution of both planets, inner in black, outer in blue.
The inner planet's eccentricity exceeds 0.99 in several instances. *Middle Left:*
The inner planet's inclination can grow larger than 160 deg. *Middle Right:* The two
resonant arguments show complicated behavior with circulation on long timescales,
but libration with large amplitude on shorter timescales. *Bottom Right:* Intellation
of the inner planet. Although typically around the Earth's solar constant of 1366
W/m^2, but increases of a factor of 30 are possible during epochs of high eccentricity.
*Bottom Right:* Energy (orange) and angular momentum (purple) are conserved to high
precision in this run. The slow drifts are typical of the 4th order Runge-Kutta scheme
in vplanet.
