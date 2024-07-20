import os
import shutil
values = list(filter(lambda x: x[-4:]=="xlsm",os.listdir(r"C:\Users\Cash\Documents\pruebas_python\proyectos\os")))

for value in values:
    if "REMOVE" in value:
        old_name = fr"C:\Users\Cash\Documents\pruebas_python\proyectos\os/{value}"
        new_name = fr"C:\Users\Cash\Documents\pruebas_python\proyectos\os\main_file/{value}"
        shutil.copy(old_name, new_name)
        
    


