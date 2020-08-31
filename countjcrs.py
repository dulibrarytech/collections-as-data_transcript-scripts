# import os package.  contains functions that allow us to easily search and manipulated directories and files
import os

# set number of pages tallied to 0
page_tally = 0

# set number of folders tallied to 0
folder_tally = 0

# define count at location process.  Takes two parameters: the file path and whether the files are tiffs
# the second parameter is optional; if ommitted has a default value of False
def count_at_location(path, tiffs=False):
    # function uses page tally and folder tally
    global page_tally
    global folder_tally
    
    # do the following for each folder/file in the given file path
    # during each iteration, the current folder/file is stored in d
    for d in os.scandir(path):    
        # if f is a directory do the following
        if d.is_dir():            
            # increase folder tally by 1
            folder_tally += 1            
            # for each folder/file in folder d do the following
            for f in os.scandir(d.path):               
                # if the file name ends with the .jpg extension or if the tiffs parameter was set to True and the
                # file name ends with .tif, do the following
                if f.name.endswith('.jpg') or (tiffs and f.name.endswith('.tif')):                    
                    # increase page tally by 1
                    page_tally += 1

# run count at location process at R:\Digital Production Services\Projects\JCRS\Spivak Extracted
count_at_location(r"R:\Digital Production Services\Projects\JCRS\Spivak Extracted", True)

# run count at location process at R:\Digital Production Services\Projects\JCRS\Treated
count_at_location(r"R:\Digital Production Services\Projects\JCRS\Treated", True)

# run count at location process at R:\Digital Production Services\Projects\JCRS\Untreated
count_at_location(r"R:\Digital Production Services\Projects\JCRS\Untreated")

# run count at location process at R:\Digital Production Services\Transkribus Datasets
count_at_location(r"R:\Digital Production Services\Transkribus Datasets")

# run count at location process at R:\Digital Production Services\Transkribus Datasets\Spivak
count_at_location(r"R:\Digital Production Services\Transkribus Datasets\Spivak")

# print to console "Folder <folder_tally>" where "<folder_tally>" is replaced with the number of folders tallied.
print("Folders: {}".format(folder_tally))

# print to console "Page <page_tally>" where "<page_tally>" is replaced with the number of pages tallied.
print("Pages: {}".format(page_tally))