'''ARCS data extraction script'''
'''User imports the path of the ARCS CD directory 
along with the ARCS ID he wishes to export.
The scripts searches the CD for the dirrectory of the chart 
and copy. 
A new directory is created where the copied folder is pasted
along with all necessary data files, required to make the new 
ARCS data be installed on an ECDIS.'''

import os, shutil

#Import ARCS CD directory path and chart ID
ARCSDIR = input("Insert ARCS CD directory:")
ChartID = input("Type ARCS chart ID:")

#Parse to extract the first 3 digits of the ARCS ID
ChartID = str(ChartID)
ThreeDigID = '0' + ChartID[0:2]

#Parse directory to move outside it
ARCSDIRNew = ARCSDIR[:-23]
os.chdir(ARCSDIRNew)

#Copy standard content
shutil.copytree(ARCSDIR, ARCSDIRNew+'/ARCS')

#Remove the RASCHTS directory with all charts data
shutil.rmtree(ARCSDIRNew+'/ARCS/RASCHTS')

#Create a new RASCHTS file with subfolder and copy chart's data 
shutil.copytree(ARCSDIR+'/RASCHTS/'+ThreeDigID+'/'+ChartID, ARCSDIRNew+'/ARCS/RASCHTS/'+ThreeDigID+'/'+ChartID)

#Create archive .zip
os.chdir(ARCSDIRNew)
shutil.make_archive('ARCS_'+ChartID, 'zip', 'ARCS')

print('Done!!!')