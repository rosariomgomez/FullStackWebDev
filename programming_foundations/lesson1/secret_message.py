import os

def rename_files():
	#get file names from folder
	file_list = os.listdir('prank/')
	saved_path = os.getcwd()
	os.chdir('prank/')
	
	#for each file, rename it
	for file_name in file_list:
		print('Old file name: ' + file_name)
		os.rename(file_name, file_name.translate(None, '1234567890'))
		print('New file name: ' + file_name.translate(None, '1234567890'))
		
	os.chdir(saved_path)

rename_files()