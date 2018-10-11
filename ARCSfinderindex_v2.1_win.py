import os, shutil
from PermitImport import PermitImport

#Import ARCS CD directory path and chart ID
ARCSDIR = input("Insert ARCS CD directory:")
#ChartID = input("Type ARCS chart ID:")

#Import 
ChartID = PermitImport()

#Create new list for three digit code. Parse the ARCS IDs to add a 0. 
ThreeDID = []
for i in ChartID:
    dig = '0' + i[0:2]
    ThreeDID.append(dig)

#Parse directory to move outside it
ARCSDIRNew = ARCSDIR[:-23]
os.chdir(ARCSDIRNew)

#Create the data folder and copy standard content within it.
shutil.copytree(ARCSDIR, ARCSDIRNew+'/ARCS')

#Remove the RASCHTS directory with all charts data
shutil.rmtree(ARCSDIRNew+'/ARCS/RASCHTS')

#Create a new RASCHTS file with subfolder and copy chart's data
for i in ThreeDID:
    shutil.copytree(ARCSDIR+'/RASCHTS/'+ThreeDID[i], ARCSDIRNew+'/ARCS/RASCHTS/'+ThreeDID[i])

    
'''
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
'''
