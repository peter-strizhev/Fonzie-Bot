from os import popen
from shutil import copy2, rmtree, copyfile
from sys import exit
from subprocess import Popen
import logging

logging.warning("INFO: Reloader has started")

Popen("python3 main.py", shell=True)

logging.warning("INFO: Reloader has finished...")
exit("Exiting to restart the main program")