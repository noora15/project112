import sys
import time
import random

import os
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# from_dir = "ENTER THE PATH OF DOWNLOAD FOLDER (USE " / ") in VSC"
# to_dir = "ENTER THE PATH OF DESTINATION FOLDER(USE " / ") in VSC"

src_path = r'C:\Users\Noona\Downloads'
dest_path = r'C:\Users\Noona\Desktop\PYTHON\P - 113\Document_files'


# Event Hanlder Class

class FileMovementHandler(FileSystemEventHandler):

    #Student Activity1
    def on_created(self, event):
        print(f'hey,{event.src_path} has been created')
    def on_deleted(self,event):    
        print(f'oops!!, someone deleted {event.src_path}!')      
    def on_modified(self,event):    
        print(f'hey there, {event.src_path} has been modified')
    def on_moved(self,event):    
        print(f'someone moved {event.src_path} to {event.dest_path}')     
       
# Initialize Event Handler Class
event_handler = FileMovementHandler()


# Initialize Observer
observer = Observer()

# Schedule the Observer
observer.schedule(event_handler, from_dir, recursive=True)


# Start the Observer
observer.start()

#Student Activity2
while True:
    time.sleep(2)
    print("running...")

    