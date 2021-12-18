import json
import os
import re
import time
import requests
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

from config import BaseConfig


class FileWatcher(FileSystemEventHandler):
    def __init__(self):
        super().__init__()
        self.config = BaseConfig()

    def on_created(self, event):
        print(event)
        try:
            # Get path to file
            get_path = event.src_path.replace('~', '')
            # Check if txt
            if bool(re.search(r'.*\.txt', get_path)) and not bool(re.search(r'CHECKED', get_path)):
                get_text = None
                with open(get_path, 'r', encoding='utf-8') as file:
                    # Read file
                    get_text = file.read()
                if get_text:
                    time.sleep(15)
                    # Send message url
                    send_telegram_url = "{url}{token}/sendMessage".format(url=self.config.TELEGRAM_API_URL,
                                                                          token=self.config.TELEGRAM_API_TOKEN)
                    send_data = requests.post(send_telegram_url,
                                              data={'chat_id': self.config.TELEGRAM_GROUP_ID, 'text': get_text,
                                                    'parse_mode': 'HTML'})
                    get_response = send_data.json()
                    # If response to telegram has error
                    if not get_response['ok']:
                        raise Exception('Error in send  message to telegram')
                    os.rename(get_path, get_path.replace('.txt', '_CHECKED.txt'))
        except Exception as e:
            print(f'Error in watch file method method.  {e}')

if __name__ == '__main__':
    path = os.path.abspath('./files')
    event_handler = FileWatcher()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=False)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except  KeyboardInterrupt:
        observer.stop()
    observer.join()
