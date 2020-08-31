import os
import subprocess

os.chdir(r"R:\Digital Production Services\Transkribus\Patient Letters\current batch")
subprocess.run('magick convert *.tif -set filename:original %t %[filename:original].jpg', shell=True)