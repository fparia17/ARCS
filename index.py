'''ARCS data extraction script'''
'''User imports the path of the ARCS CD directory 
along with the ARCS ID he wishes to export.
The scripts searches the CD for the dirrectory of the chart 
and copy. 
A new directory is created where the copied folder is pasted
along with all necessary data files, required to make the new 
ARCS data be installed on an ECDIS.'''

import os, shutil

#Import ARCS CD directory path
ARCSDIR = input("Insert ARCS CD directory:")

#Import ARCS chart ID
ChartID = input("Type ARCS chart ID:")

#Parse to extract the first 3 digits of the ARCS ID
ChartID = str(ChartID)
ThreeDigID = '0' + ChartID[0:2]

#print(ThreeDigID)
#print(os.chdir(ARCSDIR+'/RASCHTS/'+ThreeDigID+'/'+ChartID))
ChartData = os.listdir()
#print(ChartData)

#Create directory with subfolders
ARCSDIRNew = ARCSDIR[:-22]
#print(ARCSDIRNew)
os.makedirs(ARCSDIRNew+'/ARCS/CHARTCAT')
os.mkdir(ARCSDIRNew+'/ARCS/MISC')
os.makedirs(ARCSDIRNew+'/ARCS/RASCHTS/'+ThreeDigID+'/'+ChartID)

#Copy files to new directory folders
shutil.copy(ARCSDIR+'/README.CDV',ARCSDIRNew+'ARCS')


#CHARTCAT = os.listdir(ARCSDIR+'/CHARTCAT')
#print(CHARTCAT)

#Copy CHARTCAT files
shutil.copy(ARCSDIR+'/CHARTCAT/CHART.PTR',ARCSDIRNew+'/ARCS/CHARTCAT')
shutil.copy(ARCSDIR+'/CHARTCAT/CHART.CAT',ARCSDIRNew+'/ARCS/CHARTCAT')
shutil.copy(ARCSDIR+'/CHARTCAT/PLAN.CAT',ARCSDIRNew+'/ARCS/CHARTCAT')

#Copy MISC files
shutil.copy(ARCSDIR+'/MISC/COUNTRY.TAB',ARCSDIRNew+'/ARCS/MISC')
shutil.copy(ARCSDIR+'/MISC/HORDAT.TAB',ARCSDIRNew+'/ARCS/MISC')
shutil.copy(ARCSDIR+'/MISC/NOTETYPE.TAB',ARCSDIRNew+'/ARCS/MISC')
shutil.copy(ARCSDIR+'/MISC/PROJCODE.TAB',ARCSDIRNew+'/ARCS/MISC')
shutil.copy(ARCSDIR+'/MISC/UNIT.TAB',ARCSDIRNew+'/ARCS/MISC')
shutil.copy(ARCSDIR+'/MISC/VERDAT.TAB',ARCSDIRNew+'/ARCS/MISC')

#Copy chart files
shutil.copy(ARCSDIR+'/RASCHTS/'+ThreeDigID+'/'+ChartID+'/'+ChartID+'.CHI',ARCSDIRNew+'/ARCS/RASCHTS/'+ThreeDigID+'/'+ChartID)
shutil.copy(ARCSDIR+'/RASCHTS/'+ThreeDigID+'/'+ChartID+'/'+ChartID+'.CHR',ARCSDIRNew+'/ARCS/RASCHTS/'+ThreeDigID+'/'+ChartID)
shutil.copy(ARCSDIR+'/RASCHTS/'+ThreeDigID+'/'+ChartID+'/'+ChartID+'.HDR',ARCSDIRNew+'/ARCS/RASCHTS/'+ThreeDigID+'/'+ChartID)
shutil.copy(ARCSDIR+'/RASCHTS/'+ThreeDigID+'/'+ChartID+'/'+ChartID+'.LOI',ARCSDIRNew+'/ARCS/RASCHTS/'+ThreeDigID+'/'+ChartID)
shutil.copy(ARCSDIR+'/RASCHTS/'+ThreeDigID+'/'+ChartID+'/'+ChartID+'.LOR',ARCSDIRNew+'/ARCS/RASCHTS/'+ThreeDigID+'/'+ChartID)
shutil.copy(ARCSDIR+'/RASCHTS/'+ThreeDigID+'/'+ChartID+'/'+ChartID+'.N00',ARCSDIRNew+'/ARCS/RASCHTS/'+ThreeDigID+'/'+ChartID)
shutil.copy(ARCSDIR+'/RASCHTS/'+ThreeDigID+'/'+ChartID+'/'+ChartID+'.P00',ARCSDIRNew+'/ARCS/RASCHTS/'+ThreeDigID+'/'+ChartID)
shutil.copy(ARCSDIR+'/RASCHTS/'+ThreeDigID+'/'+ChartID+'/'+ChartID+'.PAL',ARCSDIRNew+'/ARCS/RASCHTS/'+ThreeDigID+'/'+ChartID)

#Create archive .zip
os.chdir(ARCSDIRNew)
shutil.make_archive('ARCS_'+ChartID, 'zip', 'ARCS')

print('Done!!!')

