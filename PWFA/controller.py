#!/usr/bin/python
######################################################################
# Name:         controller
# Author:       A. Marocchino
# Date:			25-02-2016
# Purpose:      controller for PWFA utilities: input list and plots
# Source:       python
#####################################################################

### loading shell commands
import os, os.path, glob, sys, shutil, time, datetime, scipy, pylab
from scipy import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as plt
import pylab as pyl
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
from scipy.constants import codata
#from mpl_toolkits.mplot3d import Axes3D
# - #
home_path = os.path.expanduser('~')
sys.path.append(os.path.join(home_path,'Codes/Plasma_PyCalculator/formulary'))
sys.path.append(os.path.join(home_path,'Codes/Plasma_PyCalculatorPWFA'))
from plasma_basic_parameters import *
from PWFA_calculator import *
# --- #


#--- Simple Example ---#
n0=1e17*1e6 #density in m^-3
k0    = electron_plasma_wavenumber(n0)
lambda_p = electron_plasma_wavelength(n0)
print (lambda_p*1e6)
sys.exit('stopped script')
