import shutil
import os
import sys
import time
import random
from watchdog.events import FileSystemEventHandler 
from watchdog.observers import Observer

from_dir="C:\\Users\\satis\\Downloads"
to_dir="F:\\game\\Python\\class activity\\class 103\\download_file"

dir_tree={
    "image_files":[".gif",".png",".jfif",".jpeg",".jpg"],
    "video_files":[".mpg",".mp2",".mpeg",".mp3",".mp4",".mpv",".mpe",".m4p",".m4v",".avi",".mov",".avchd"],
    "document_files":[".doc",".docx",".xls",".xlsx",".txt",".pdf",".csv",".py",".ppt",".pptx"],
    "setup_files":[".exe",".bin",".cmd",".msi",".dmg"]
}

class FileMovementHandler(FileSystemEventHandler):
    def on_created(self,event):
        print("working........!")
        root,ext=os.path.splitext(event.src_path)
        time.sleep(1)

        for key,value in dir_tree.items():
            print("jhfhdgasuy")
            time.sleep(1)

            if(ext in value):
                file_name=os.path.basename(event.src_path)
                print("downloaded"+file_name)

                path1=from_dir+"/"+ file_name
                path2=to_dir+"/"+key
                path3=to_dir+"/"+key+"/"+ file_name

                if(os.path.exists(path2)):
                    print("Moving"+file_name+"....")
                    shutil.move(path1,path3)
                    time.sleep(1)
                else:
                    print("making directories")
                    os.makedirs(path2)
                    print("Moving"+file_name+"....")
                    shutil.move(path1,path3)
                    time.sleep(1)

event_handler = FileMovementHandler()
observer = Observer()
observer.schedule(event_handler,from_dir,recursive=True)
observer.start()

try:
    while True:
         time.sleep(2)
         print("running...") 
except KeyboardInterrupt:
    print("stopped!")
    observer.stop()