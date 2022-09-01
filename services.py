import subprocess
import time

PATH = "C:/Users/Karlo/Desktop/"

def call_R_script(name : str):
    subprocess.call ("Rscript --vanilla " + PATH + name +  ".R", shell=True)

def get_position(strategy : str):
    if strategy == 'DM':
        R_script_name = 'DM_features'
        ##Ovdje pozvati prvo izgradnju featura s R skriptom
        subprocess.call ("Rscript --vanilla " + PATH +  + R_script_name +".R", shell=True)
        ##Pricekaj da se generiraju featurei
        time.sleep(1)
        ##Zatim pozvati poziciju s istim featurima

        pass

if __name__ == "__main__":
    call_R_script("probar")