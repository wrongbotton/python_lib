
from __future__ import print_function
import pandas
import pandas as pd
from PIL import Image
import scipy.io, os, sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from collections import OrderedDict
import scipy.misc
import matplotlib as mpl
from matplotlib import colors
import glob


CAFFECODEROOT=os.path.expandvars('/workspace2/Code/caffe')
CAFFESUB='dev'
def generate_caffepath(caffecoderoot,caffesub,buildpath='build/tools/caffe'):   
    caffepythonpath=os.path.join(caffecoderoot,caffesub,'python')
    caffeexepath=os.path.join(caffecoderoot,caffesub,buildpath)
    caffeextraspath=os.path.join(caffecoderoot,caffesub,'tools/extra')
    logdir=os.path.join(caffecoderoot,'logs/')
    traineddir=os.path.join(caffecoderoot,'trained-models')
    workdir=os.path.join(caffecoderoot,'models')
    return caffepythonpath,caffeexepath,caffeextraspath,logdir,traineddir,workdir
    

CAFFEPYTHONPATH,CAFFEEXEPATH,CAFFEEXTRASPATH,LOGDIR,TRAINEDDIR,WORKDIR =  generate_caffepath(CAFFECODEROOT,CAFFESUB)


# print("CAFFEPYTHONPATH: "+CAFFEPYTHONPATH,
#     "CAFFEEXEPATH: "+CAFFEEXEPATH,
#     "CAFFEEXTRASPATH: "+CAFFEEXTRASPATH,
#     "LOGDIR: "+LOGDIR,
#     "TRAINEDDIR: "+TRAINEDDIR,
#     "WORKDIR: "+WORKDIR,
#     sep='\n')
