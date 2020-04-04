import time
import os
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

docExt = [".doc", ".docx", ".odt", ".pdf", ".rtf", ".tex", ".txt", ".wks", ".wps", ".wpd", ".xps", ".vsdx", ".xls", ".xlsx"]
photoExt = [".jpg", ".jpeg", ".png", ".gif", ".tiff", ".psd", ".eps", ".ai", ".raw", ".indd", ".cdr", ".svg"]
musicExt = [".aac", ".aif", ".aiff", ".iff", ".m3u", ".m4a", ".mid", ".mp3", ".mpa", ".oga", ".ra", ".wav", ".wma"]
othersExt = [".exe", ".zip", ".rar", ".7z", ".torrent", ".mp4", ".ct", ".avi"]

class Watcher:
    DIRECTORY_TO_WATCH = "E:\Pobrane"

    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print ("Error")

        self.observer.join()

class FileMover:
    def move(self, name, ext, src_dir):
        dest_photo = "E:\\Zdjęcia\\"
        dest_music = "E:\\Muzyka\\"
        dest_others = "E:\\Inne\\"
        dest_doc = "E:\\Dokumenty\\"

        fc = FileChecker()

        try:
            if ext in photoExt:
                time.sleep(2)
                fc.checker(src_dir, dest_photo, name)
            elif ext in docExt:
                time.sleep(2)
                fc.checker(src_dir, dest_doc, name)
            elif ext in musicExt:
                time.sleep(2)
                fc.checker(src_dir, dest_music, name)
            elif ext in othersExt:
                time.sleep(2)
                fc.checker(src_dir, dest_others, name)
        except:
            pass

class FileChecker:
    def checker(self, src_dir, dest_dir, name):
        try:
            with open(dest_dir + name) as f:
                name = "new_" + name
                self.checker(src_dir, dest_dir, name)
        except IOError:
            os.rename(src_dir, dest_dir + name)
            shutil.move(src_dir, dest_dir + name)
        finally:
            f.close()

class Handler(FileSystemEventHandler):

    @staticmethod
    def on_any_event(event):
        if event.is_directory:
            return None

        elif event.event_type == 'created' or event.event_type == 'modified':
            try:
                fm = FileMover()
                src = event.src_path
                filename, file_extension = os.path.splitext(src)
                name = os.path.basename(src)
                time.sleep(2)
                fm.move(name, file_extension, src)
            except Exception:
                pass

if __name__ == '__main__':
    w = Watcher()
    w.run()
