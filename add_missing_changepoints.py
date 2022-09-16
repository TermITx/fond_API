
import subprocess
if __name__ == "__main__":
    #call_yahoo_from_start()
    #call_yahoo()
    #my_worker.main(21)
    command = ["python" ,  "-m" ,  "model.examples.my_worker" ,    "21"]
    process = subprocess.Popen(command)
    process.wait()
    ##call_R_script("probar")