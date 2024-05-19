import pyautogui as py
import time

py.PAUSE = 2.5
py.FAILSAFE = True

# Main function 
# Initialize the script
# MAXIMUM TIME OF EXECUTION : 600 seconds = 10 min
def main():

    # Initial time
    start = time.time()

    # Total time of execution
    delta = 0

    # MAXIMUM TIME OF EXECUTION
    time_limit = 600
        
    while(delta <= time_limit ):


        try:
            X,Y = py.locateCenterOnScreen("../img/lol/img_01.png",confidence=0.7)
        except :
            #print("Imagen no encontrada")
            continue
        else:
            py.moveTo(X,Y,duration=0.2)
            time.sleep(0.3)
            py.click(clicks=2,interval=0.2)
            print(X,Y)
            print("Imagen encontrada")
            break
        
        finally:
            delta = time.time() - start

        

    return   