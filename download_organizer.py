from datetime import datetime
import os
import shutil
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class DownloadOrganizerHandler(FileSystemEventHandler):
    def on_created(self, event):
        try:
            # Ignore temporary files and other possible problematic files
            if event.src_path.endswith('.tmp') or event.src_path.endswith('.crdownload'):
                return

            today = datetime.now().strftime('%d-%m-%Y')
            folder_name = os.path.join(downloads_path, today)
            if not os.path.exists(folder_name):
                os.makedirs(folder_name)
            if not event.is_directory:
                self.move_file_with_retry(event.src_path, folder_name)
        except Exception as e:
            print(f"Error handling file {event.src_path}: {e}")

    def move_file_with_retry(self, src_path, dest_folder, attempt=1, max_attempts=5):
        try:
            time.sleep(10)
            shutil.move(src_path, dest_folder)
            print(f"File {os.path.basename(src_path)} successfully moved to {dest_folder}.")
        except FileNotFoundError:
            print(f"File {src_path} not found. It may have been moved or deleted.")
        except PermissionError as e:
            if attempt <= max_attempts:
                print(f"Permission error for {src_path}: {e}. Retrying in 2 seconds. Attempt {attempt}/{max_attempts}.")
                time.sleep(10)  # Wait a bit before retrying
                self.move_file_with_retry(src_path, dest_folder, attempt + 1, max_attempts)
            else:
                print(f"Failed to move {src_path} after {max_attempts} attempts. It may be in use by another process.")

# Path to your downloads directory or any other directory you want to monitor
downloads_path = "C:\\Users\\<User>\\Downloads"

if __name__ == "__main__":
    event_handler = DownloadOrganizerHandler()
    observer = Observer()
    observer.schedule(event_handler, downloads_path, recursive=False)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
