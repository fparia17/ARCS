'''Open the permit files and export the included IDs.'''

def PermitImport():
	#Create an empty list
	ChartsID = []

	#Open permit file, parse each line and add to the ChartsID list
	with open('GB.NCP','r') as f:
		for line in f:
			for word in line.split():
				ChartsID.append(word[:4])

	#Close file
	f.close()

	#Create an new empty list
	ChartsID_new = []

	#Remove + sign from ChartsID list and add new item to ChartsID_new list.
	for i in ChartsID:
		new = i.replace("+", "")
		ChartsID_new.append(new)
	
	return ChartsID_new
	

