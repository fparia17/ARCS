		
		ARCS Data Finder
		================
		
This application allows the user export any ARCS chart's data from the provided
base CD, to a compress zip file.

User will be requested to add the ARCS Base CD path directory and import chart's 
ID to export. 
The application will create an "ARCS_Data" folder and add the data of the provided
ARCS ID to it. The user will then be asked if more charts' data needs to be added 
to the "ARCS_Data" folder. The loop continues until negative input is provided by 
the user.
Once done the "ARCS_Data" folder is compressed to "ARCS_Data.zip" file. 
The directory path is given to the user for easy access of the file.
The exported file may then be send to the customer/vessel, to di-compress and 
install on vessel's ECDIS.

The application is developed in Python programming language.
