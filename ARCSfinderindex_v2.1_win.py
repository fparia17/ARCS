import os, shutil

while True:
    #Import ARCS CD directory path and chart ID
    ARCSDIR = input("Insert ARCS CD directory:")
    ChartID = input("Type ARCS chart ID:")
    
    #Info messages to the user
    print('"ARCS_Data" folder created!')
    print("Coping chart's data to folder...")
    
    #Parse to extract the first 3 digits of the ARCS ID
    ChartID = str(ChartID)
    ThreeDigID = '0' + ChartID[0:2]

    #Parse directory to move outside it
    ARCSDIRNew = ARCSDIR[:-23]
    os.chdir(ARCSDIRNew)
    
    #If the ARCS folder exists do not created and add chart data
    if os.path.exists(ARCSDIRNew+'/ARCS'):
        print('''Adding chart's data to "ARCS_Data" folder...''')
        shutil.copytree(ARCSDIR+'/RASCHTS/'+ThreeDigID+'/'+ChartID, ARCSDIRNew+'/ARCS/RASCHTS/'+ThreeDigID+'/'+ChartID)
    else:                  #If ARCS folder does not exist, created and add initial data
        #Copy standard content
        shutil.copytree(ARCSDIR, ARCSDIRNew+'/ARCS')
        #Remove the RASCHTS directory with all charts data
        shutil.rmtree(ARCSDIRNew+'/ARCS/RASCHTS')
        #Create a new RASCHTS file with subfolder and copy chart's data 
        shutil.copytree(ARCSDIR+'/RASCHTS/'+ThreeDigID+'/'+ChartID, ARCSDIRNew+'/ARCS/RASCHTS/'+ThreeDigID+'/'+ChartID)
    
    #Ask user if more chart data need to be added to teh ARCS directory
    choice = input("\nAdd another chart? y/n:")
    if choice == 'y':
        continue
    else:
        break

#Create archive .zip
os.chdir(ARCSDIRNew)
shutil.make_archive('ARCS_Data', 'zip', 'ARCS')

#Info messages to the user
print('\n==========================================\n')
print('Done!!!\nCompressed file ready.')
print('"ARCS_Data.zip" available at, path:'+ARCSDIRNew)
