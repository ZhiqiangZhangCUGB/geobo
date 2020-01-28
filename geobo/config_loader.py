# config_loader.py

import yaml
import os
import numpy as np

with open('settings.yaml') as f:
	cfg = yaml.safe_load(f)

for key in cfg:
	globals()[str(key)] = cfg[key]

xLcube = xmax - xmin # x Lenght of cube in meters. 
yLcube = ymax - ymin # y Lenght of cube in meters. 

zmin = zmax - zLcube

magneticField = np.asarray([XMAG, YMAG, ZMAG]) * 1e-3 

fname_drilldata = outpath + FNAME_drilldata
fname_gravsurvey = inpath + FNAME_gravsurvey
fname_magsurvey = inpath + FNAME_magsurvey


c_MILLIGALS_UNITS = c_G * c_SI_TO_MILLIGALS * c_GCM3_TO_SI

# Some other capre-caculations to define parameters
xvoxsize = xLcube / xNcube * 1. # size of one voxel in meters
yvoxsize = yLcube / yNcube * 1. # size of one voxel in meters
zvoxsize = zLcube / zNcube * 1. # size of one voxel in meters
Nsensor = xNcube * yNcube