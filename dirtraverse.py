"""
This function takes the name of a directory 
and prints out the paths files within that 
directory as well as any files contained in 
contained directories. 
Don't use os.walk
"""

def print_directory_contents(path):
    import os
    for child in os.listdir():
    	childpath = os.path.join(path,child)
    	if os.path.isdir(chilpath):
    		print_directory_contents(chilpath)

    	else:
    		print(childpath)


 # Important notes 
 # os.path.join is needed for cross-operating system compatibility. as path+'/'+child wouldn't work on Windows
 