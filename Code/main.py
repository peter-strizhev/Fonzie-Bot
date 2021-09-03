# Imports
from multiprocessing import Process
from subprocess import Popen
import urllib.request
import logging
import time
import Bot

# Threading Bot Thread
p1 = Process(target=Bot.launch)

######################## Github Implementation
def GithubDownload():
    botURL = "https://raw.githubusercontent.com/Shrewkin/Fonzie-Bot/main/Code/Bot.py"
    logging.info("INFO: File Download has started...")
    filename, headers = urllib.request.urlretrieve(botURL, filename="Bot.py")
    logging.warning("INFO: Download Complete")
    logging.warning("DEBUG: Downloaded Bot.py into directory: ", filename)
    logging.warning("DEBUG: Downloaded Headers: \n", headers)

########################### AutoUpdater
def UpdateLoop():
    starttime = time.time()
    interval = 1

    # Update Loop
    while True:

        # Number of seconds in a day
        #counter = 86400
        counter = 5
        while counter != 0:
            time.sleep(interval - ((time.time() - starttime) % interval))
            counter -= 1
        
        p1.terminate()
        GithubDownload()
        
        Popen("python3 reloader.py", shell=True) # start reloader

        exit("Exiting and updating files...")

# Threading UpdateLoop Thread
p2 = Process(target=UpdateLoop)

def main():
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    
main()