import subprocess
import time

import model.call_model as model
import model.examples.my_worker as my_worker
import model.combine_all_feature as combine_all_features
PATH = "C:/Users/Karlo/Desktop/"

def call_R_script(name : str):
    subprocess.call ("Rscript --vanilla " + PATH + name +  ".R", shell=True)

def get_position(strategy : str):
    print(strategy)
    if strategy == 'DM':
        print("uso")
        R_script_name = 'DM_features'
        ##Ovdje pozvati prvo izgradnju featura s R skriptom
        #subprocess.call ("Rscript --vanilla " + PATH +  + R_script_name +".R", shell=True)
        ##Pricekaj da se generiraju featurei
        #time.sleep(1)
        ##Zatim pozvati poziciju s istim featurima

        #my_worker.main(21)
        #my_worker.main(126)
        command = ["python" ,  "-m" ,  "model.examples.create_features_quandl" ,   "126",   "21"]
        process = subprocess.Popen(command)

        #subprocess.call ("python " +  "-m " +  "model.examples.create_features_quandl " +   "126 "  + "21 ", shell=True)

        #combine_all_features.combine_all_features()

        return model.call_model()

        

if __name__ == "__main__":
    call_R_script("probar")