# Spero GeoClawPortAngeles #
**Title: GeoClaw Code for Numerically Modeling Hypothetical Earthquake Ruptures in the Strait of Juan de Fuca.** 

## **Overview:** ## 
ReadMe file created by Hannah Spero to complement submission to IJURCA (International Journal of Undergraduate Research and Creative Activities). The IJURCA submission prepared by Spero, H.(1), Petersen, N. J.(2), and MacInnes, B.(3). (1) Boise State University Department of Geosciences, (2) Central Washington University, Accessibility Studies Program Coordinator, and (3) Central Washington University, Department of Geological Sciences. 

This research aims to model Cascadia Subduction Zone (CSZ) earthquakes (M<sub>w</sub> 8.7 - 9.2), hypothetical Leech River Fault (LRF) earthquakes (M<sub>w</sub> 7.3 - 7.5), and one hypothetical Utsalady Point Fault (UPF) earthquakes(M<sub>w</sub> 7.0) and the resulting tsunamis. “From these earthquakes we used GeoClaw version 5.4.1 to calculate the resulting tsunamis at Port Angeles, Washington” Results were compared with the 2017 Port Angeles Hazards Map prepared by the WA-DNR and analyzed with universal design in mind for risk assessment.

## **Features** ##
#### (1) [Topography file (MHW datum, 1/3 arc-second resolution, NAVD '88 :globe_with_meridians:)](https://catalog.data.gov/dataset/strait-of-juan-de-fuca-1-3-arc-second-navd-88-coastal-digital-elevation-model) ####
##### "To simulate flow over topography it is necessary to specify the topography. Our .topo files are provided in ASCII format for ease of use. #####
      
#### (2) maketopo.py file ####
##### The maketopo.py file is needed to remake the earthquakes, earthquake variables based on table below (references in IJURCA). #####
| FileName  | Location |M<sub>w</sub>| Longitude* | Latitude* | Strike | Length (km) | Width (km) | Depth (km) | Rake | Dip | Slip (m) |
| ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |
| UtsaladyMw70_90dip_4m | Utsalady  | 7.0 | -122.60000 | 48.30000 | 298 | 29 | 8 | 0 | 90 | 90 | 4 |
| LR2Mw75_60km_75dip_5m  | LRF  | 7.5 | -123.06538 | 48.366628 | 294 | 60 | 15 | 0 | 90 | 75 | 5 |
| LR1Mw75_60km_75dip_5m  | LRF  | 7.5 | -123.094417 | 48.304968 | 294 | 60 | 15 | 0 | 90 | 75 | 5 |
| LR1Mw75_60km_60dip_5m  | LRF  | 7.5 | -123.094417 | 48.304968 | 294 | 60 | 15 | 0 | 90 | 60 | 5 |
| LR1Mw73_W30km_60dip_5m  | LRF  | 7.3 | -123.27779 | 48.359396 | 294 | 30 | 15 | 0 | 90 | 60 | 5 |
| LR1Mw73_E30km_60dip_5m  | LRF | 7.3 | -122.87462 | 48.304968 | 294 | 30 | 15 | 0 | 90 | 60 | 5 |

*up-dip center point

#### (3) [.dtopo plots for CSZ, LRF, and UPF deformation](https://www.clawpack.org/geoclaw/dtopotools_examples.html) ####
##### Shows deformation produced on the sea floor for each of the modeled sources including the LRF and UPF sources. This repository has a folder containing the sea surface deformation images for reference. The Cascadia sources and plots of the sea surface deformation were provided by Dr. Randy LeVeque and are based on those used in: (links at bottom of README.md*)
       (1) Simulated tsunami inundation for a range of Cascadia megathrust earthquake scenarios at Bandon, Oregon, USA, by R. C. Witter and Y. Zhang and K. Wang and G. R. Priest and C. Goldfinger and L. L. Stimely and J. T. English and P. A. Ferro, Geosphere (2013) pp. 1783-1803.
       (2) Simulating tsunami inundation at Bandon, Coos County, Oregon, using hypothetical Cascadia and Alaska earthquake scenarios, by R. C. Witter and Y. Zhang and K. Wang and G. R. Priest and C. Goldfinger and L. L. Stimely and J. T. English and P. A. Ferro, Oregon Department of Geology and Mineral Industries Special Paper 43, 2011. ####
       (3) Probabilistic Tsunami Hazard Assessment (PTHA) for Crescent City, CA. Final Report, by Frank I. Gonzalez, Randall J. LeVeque, Loyce M. Adams, Chris Goldfinger, George R. Priest, and Kelin Wang, 2014. ####

#### (4) [Setrun.py](https://www.clawpack.org/setrun_geoclaw.html) ####
##### The setrun file will have all the info about simulation length :clock930: and timestep :clock930:- a python script contains runtime parameters for given problem a GeoClaw simulation only requires modifying setrun.py (and providing bathymetry and fault source files) #####
#### (5) [Gauges and stationary gauge plots :pushpin:](https://www.clawpack.org/gauges.html) ####
#### (6) fgmax python file for creating the inundation plots ####

## **Running the project** ##
#### Please reference Clawpack documentation for how to use the the GeoClaw Software to answer additional questions. We recommend you using the [GitHub repository link to the GeoClaw code files of version 5.4.1](https://github.com/clawpack/doc/blob/dev/doc/geoclaw.rst) and the [instructions for getting started in v.5.4.1](https://www.clawpack.org/v5.4.x/geoclaw.html)
#### General commands to run from a terminal window in Python or a WSL command line: ####
       (1) cd to the right directory depending on your file hierarchy
              (i) example: cd $clawpack/geoclaw/examples/tsunami/GeoClawPortAngelesWashington
       (2) $ make help (list of options)
       (3) $ make topo (calls on the topography for usage)
       (4) $ make data (uses setrun.py to make Fortrain input)
       (5) $ make exe (compiles the Fortran code)
       (5) $ make outputs (runs code and produces _output/ folder)
       (6) $ make plots (plots results in _plots/ folder)
       (7) $ make htmls (produces html verisons of files and README.txt)
       
## **Contact** ##
Hannah Spero
Twitter - [@sperogeology](https://twitter.com/SperoGeology)

Email :mailbox: - hannahspero11@gmail.com

## Contributors :ocean:
GeoClaw parameters set by: Hannah Spero and Breanyn MacInnes. Also thanks to Bryce Coleman who designed the UPF scenarios and Trent Adams who designed the LRF scenarios, who were both CWU undergraduates. 
## Provided links to earthquake scenario papers ##
[Simulated tsunami inundation for a range of Cascadia megathrust earthquake scenarios at Bandon, Oregon, USA, by R. C. Witter and Y. Zhang and K. Wang and G. R. Priest and C. Goldfinger and L. L. Stimely and J. T. English and P. A. Ferro, Geosphere (2013) pp. 1783-1803.](https://pubs.geoscienceworld.org/gsa/geosphere/article/9/6/1783/132896/Simulated-tsunami-inundation-for-a-range-of) 

[Simulating tsunami inundation at Bandon, Coos County, Oregon, using hypothetical Cascadia and Alaska earthquake scenarios, by R. C. Witter and Y. Zhang and K. Wang and G. R. Priest and C. Goldfinger and L. L. Stimely and J. T. English and P. A. Ferro, Oregon Department of Geology and Mineral Industries Special Paper 43, 2011.](https://www.oregongeology.org/tsuclearinghouse/resources/sp-43/SP-43_onscreen144dpi.pdf)

[Probabilistic Tsunami Hazard Assessment (PTHA) for Crescent City, CA. Final Report, by Frank I. Gonzalez, Randall J. LeVeque, Loyce M. Adams, Chris Goldfinger, George R. Priest, and Kelin Wang, 2014.](http://hdl.handle.net/1773/25916)
