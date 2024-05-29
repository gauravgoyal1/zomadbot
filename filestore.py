import json
import os

class FileStore:
    def __init__(self):
        self.filename = "data.json"
        # Initialize the file if it does not exist
        if not os.path.exists(self.filename):
            with open(self.filename, 'w') as file:
                json.dump({}, file)

    def add(self, key, value):
        key = str(key)
        with open(self.filename, 'r+') as file:
            data = json.load(file)
            data[key] = value
            file.seek(0)
            json.dump(data, file, indent=4)
    
    def fetch(self, key):
        key = str(key)
        with open(self.filename, 'r') as file:
            data = json.load(file)
            return data.get(key, None)

    def remove(self, key):
        key = str(key)
        with open(self.filename, 'r+') as file:
            data = json.load(file)
            if key in data:
                del data[key]
                file.seek(0)
                file.truncate()
                json.dump(data, file, indent=4)
    
    def list_keys(self):
        with open(self.filename, 'r') as file:
            data = json.load(file)
            return list(data.keys())