


from os.path import isfile as existe_ruta_y_arch

ruta_y_arch="../filesPy/firefox.csv"

def checkfile_2(ruta_y_arch):
	if existe_ruta_y_arch(ruta_y_arch):
		print ("El fichero existe") 
	else: 
		print ("El fichero no existe")

checkfile_2(ruta_y_arch) 
