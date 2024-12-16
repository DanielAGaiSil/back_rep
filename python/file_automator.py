import os   #For interacting with the operating system, such as scanning directories and handling file paths 
import sys  #For handling command-line arguments
import time  #For adding sleep delays
import logging #For creating logs to track events
import schedule  #For automating the script, in order to run every day
from watchdog.observers import Observer  #To monitor file system events
from watchdog.events import LoggingEventHandler  #A built-in event handler to log events
from time import sleep #Already imported time for delays

# Getting your source directory (in my case:"/Users/Daniel/Downloads") where the program will grab your downloaded files
# with os.scandir("/Users/Daniel/Downloads") as entries:
#     for entry in entries:
#         print(entry.name) <----- This code is just for you to check if your source directory is correct, printing all its elements

#Define a handler for sorting files based on their type
class FileSorterHandler(LoggingEventHandler):
    #This class handles file system events and sorts newly created files 
    #in the monitored directory into categorized subdirectories 
    #(e.g., Documents, Images, Videos).
    def __init__(self, source_dir):
        #Initializes the FileSorterHandler class.
        #Parameters:
        #source_dir (str): The source directory that the script monitors for new files.
        super().__init__() #Call the parent class constructor to initialize the base event handling functionality.
        self.source_dir = source_dir #Store the source directory path as a class attribute to reference when sorting files.

    def on_created(self, event):
        #Triggered when a new file is created in the monitored folder.
    
        if not event.is_directory:  #Ignore directory creation events
            sleep(2)  # Delay to ensure the file is fully downloaded
            self.sort_file(event.src_path)

    def sort_file(self, file_path):
        
        #Sorts a single file into the appropriate folder based on its type.

        file_type_dirs = {
            #The first bit is the most important, rename these to all the folders (folders that will be created in the download directory)
            #you want your files to be, and you can mix them around (e.g., have my images and videos together)
            #then just copy the list of images to videos or vice-versa.
            'Documentos': ['.pdf', '.docx', '.txt', '.xlsx'],
            'Imagens': ['.jpg', '.jpeg', '.png', '.gif'],
            'Videos': ['.mp4', '.mkv', '.avi'],
            'Músicas': [".mp3", ".wav", ".flac", ".mkv"],
            'Other': []  # Uncategorized files
        }

        if os.path.isfile(file_path):  # Ensure it's a file
            _, ext = os.path.splitext(file_path)  # Extract the file extension
            destination = 'Other'  # Default folder for uncategorized files

            #Match the file's extension to its respective folder
            for folder, extensions in file_type_dirs.items():
                if ext.lower() in extensions:
                    destination = folder
                    break

            #Create the target directory if it doesn’t exist
            dest_dir = os.path.join(self.source_dir, destination)
            os.makedirs(dest_dir, exist_ok=True)

            #Move the file to the appropriate folder
            new_path = os.path.join(dest_dir, os.path.basename(file_path))
            os.rename(file_path, new_path)
            logging.info(f"Moved {os.path.basename(file_path)} to {destination}")


#Entry point of the script
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')

    source_directory = "/Users/Daniel/Downloads"  # Change this to your source folder

    #Create and set up the event handler
    event_handler = FileSorterHandler(source_directory)

    #Create and start the observer
    observer = Observer()
    observer.schedule(event_handler, source_directory, recursive=False)  # Non-recursive for simplicity
    observer.start()

    try:
        while True:
            time.sleep(5)  #Keep the program running to monitor new events
    except KeyboardInterrupt:
        observer.stop()  #Stop observing on user interrupt
    observer.join()  #Wait for the observer to finish shutting down