# Spero GeoClawPortAngeles #
**Title: GeoClaw Code for Numerically Modeling Hypothetical Earthquake Ruptures in the Strait of Juan de Fuca.** 

## **Overview:** ## 
ReadMe file created by Hannah Spero to compliment submission to IJURCA (International Journal of Undergraduate Research and Creative Activities). The IJURCA submission prepared by Spero, H.(1), Petersen, N. J.(2), and MacInnes, B.(3). (1) Boise State University Department of Geosciences, (2) Central Washington University, Accessibility Studies Program Coordinator, and (3) Central Washington University, Department of Geological Sciences. 

This research aims to model Cascadia Subduction Zone (CSZ) earthquakes (Mw 8.7 - 9.2), hypothetical Leech River Fault (LRF) earthquakes (Mw 6.8 - 7.5), and hypothetical Utsalady Point Fault (UPF) earthquakes(Mw 6.8 - 7.5) and the resulting tsunamis. Here, Mw = magnitude. From this research we determined corresponding tsunami sizes for Port Angeles, Washington. Results were compared with the 2017 Port Angeles Hazards Map prepared by the WA-DNR and analyzed with universal design in mind for risk assessment.

## **Features** ##
#### (1) [Topography file (MHW datum, 1/3 arc-second resolution, NAVD '88 :globe_with_meridians:)](https://catalog.data.gov/dataset/strait-of-juan-de-fuca-1-3-arc-second-navd-88-coastal-digital-elevation-model) ####
##### "To simulate flow over topography it is of course necessary to specify the topography. This is usually done by providing one or more files of surface elevation (relative to some reference, e.g. sea level) at a set of points on a rectangular grid (with x-y locations in Cartesian units or in latitude-longitude, depending on the application). Several file formats are recognized by GeoClaw. See Topography data for more information on how to specify topography and some on-line resources for obtaining topography" -Clawpack Creators. Our files are provided in ASCII format for ease of use. #####
      
#### (2) [Makedata file (shows initial conditions and files being used in current runs)](https://www.clawpack.org/makefiles.html) ####
#### (3) [.dtopo plots for CSZ, LRF, and UPF deformation](https://www.clawpack.org/geoclaw/dtopotools_examples.html) ####
##### Shows deformation produced on the sea floor for each of the modeled sources including the LRF and UPF sources #####
#### (4) [Setrun.py](https://www.clawpack.org/setrun_geoclaw.html) ####

##### python script contains runtime parameters for given problem a GeoClaw simulation only requires modifying setrun.py (and providing bathymetry and fault source files) #####
#### (5) [Setplot.py](https://www.clawpack.org/setplot.html) ####
#### (6) [Gauges and Stationary Gauge Plots :pushpin:](https://www.clawpack.org/gauges.html) ####


## **Running the Project** ##
### Please reference Clawpack documentation for how to use the [GeoClaw Software](http://www.clawpack.org/geoclaw) ###
#### Generally to run from a terminal window in Python or a WSL command line: ####
       (1) cd to the right directory depending on your file hierarchy
              (i) example: cd $clawpack/geoclaw/examples/tsunami/GeoClawPortAngelesWashington
       (2) $ make help (list of options)
       (3) $ make topo (calls on the topography for usage)
       (4) $ make data (uses setrun.py to make Fortrain input)
       (5) $ make exe (compiles the Fortran code)
       (5) $ make outputs (runs code and produces _output/ folder)
       (6) $ make plots (plots results in _plots/ folder)
       (7) $ make htmls (produces html verisons of files and README.txt)
       
### Parameters: ###
##### (i) :clock930: Simulation Run Time  = 48 hours = 172800 sec #####
##### (ii) :clock930: Time Step = 0.5 sec #####


## **Table of Tested Sources (rupture, length, width, fault drip, slip, etc.** ##
## **Contact** ##
Hannah Spero
Twitter - [@sperogeology](https://twitter.com/SperoGeology)

Email :mailbox: - hannahspero11@gmail.com

## Contributors :ocean:
Code development by: Breanyn MacInnes and Hannah Spero. Also thanks to Bryce Coleman who designed the UPF scenarios and Trent Adams who designed the LRF scenarios, who were both CWU undergraduates. 
