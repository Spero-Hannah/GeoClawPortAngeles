"""
Create topo and dtopo files needed for this example:
    etopo10min120W60W60S0S.asc        download from GeoClaw topo repository
    dtopo_usgs100227.tt3              create using Okada model
Prior to Clawpack 5.2.1, the fault parameters we specified in a .cfg file,
but now they are explicit below.

Call functions with makeplots==True to create plots of topo, slip, and dtopo.
"""

from __future__ import absolute_import
from __future__ import print_function
import os

import clawpack.clawutil.data

try:
    CLAW = os.environ['CLAW']
except:
    raise Exception("*** Must first set CLAW enviornment variable")



def make_dtopo(makeplots=False):
    """
    Create dtopo data file for deformation of sea floor due to earthquake.
    Uses the Okada model with fault parameters and mesh specified below.
    """
    from clawpack.geoclaw import dtopotools
    import numpy

    dtopo_fname = os.path.join("BRE_LR2_30km_5mEhalf.tt3")

    # Specify subfault parameters for this simple fault model consisting
    # of a single subfault:

    usgs_subfault = dtopotools.SubFault()
    usgs_subfault.strike = 294.
    usgs_subfault.length = 30.e3
    usgs_subfault.width = 15.e3
    usgs_subfault.depth = 0.e3
    usgs_subfault.slip = 5
    usgs_subfault.rake = 90.
    usgs_subfault.dip = 60.
    usgs_subfault.longitude = -122.86371
    usgs_subfault.latitude = 48.340815
    usgs_subfault.coordinate_specification = "top center"

    fault = dtopotools.Fault()
    fault.subfaults = [usgs_subfault]

    print("Mw = ",fault.Mw())

    if os.path.exists(dtopo_fname):
        print("*** Not regenerating dtopo file (already exists): %s" \
                    % dtopo_fname)
    else:
        print("Using Okada model to create dtopo file")

        x = numpy.linspace(-127, -122, 301)
        y = numpy.linspace(46, 51, 301)
        times = [1.]

        fault.create_dtopography(x,y,times)
        dtopo = fault.dtopo
        dtopo.write(dtopo_fname, dtopo_type=3)


    if makeplots:
        from matplotlib import pyplot as plt
        if fault.dtopo is None:
            # read in the pre-existing file:
            print("Reading in dtopo file...")
            dtopo = dtopotools.DTopography()
            dtopo.read(dtopo_fname, dtopo_type=3)
            x = dtopo.x
            y = dtopo.y
        plt.figure(figsize=(12,7))
        ax1 = plt.subplot(121)
        ax2 = plt.subplot(122)
        fault.plot_subfaults(axes=ax1,slip_color=True)
        ax1.set_xlim(x.min(),x.max())
        ax1.set_ylim(y.min(),y.max())
        dtopo.plot_dZ_colors(1.,axes=ax2)
        fname = os.path.splitext(os.path.split(dtopo_fname)[-1])[0] + '.png'
        plt.savefig(fname)
        print("Created ",fname)


if __name__=='__main__':
#    get_topo(False)
    make_dtopo(False)
