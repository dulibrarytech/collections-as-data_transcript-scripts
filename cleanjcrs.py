import os
import shutil


for dir_1 in os.scandir(r"R:\Digital Production Services\Department Projects\JCRS\Patient Letter Treated"):
    if dir_1.is_dir():
        for dir_2 in os.scandir(dir_1.path):
            if dir_2.is_dir() and dir_2.name == 'out':
                for f in os.scandir(dir_2.path):
                    if f.name.endswith(".jpg") or f.name.endswith(".tif"):
                        os.rename(f.path, dir_1.path + "\\" + f.name)
                shutil.rmtree(dir_2.path)
            else:
                try:
                    os.remove(dir_2.path)
                except PermissionError:
                    pass
                    