from watchdog.events import FileSystemEventHandler
import os 

class FileHandler(FileSystemEventHandler):
    def __init__(self, update_callback):
        super().__init__()
        self._update_callback = update_callback
        self.script_path = os.path.dirname(os.path.abspath(__file__))
        self.instructions_file_path = os.path.join(self.script_path, 'Instructions.txt')

    def read_file(self):
        with open(self.instructions_file_path, 'r') as file:
            self.instructions = file.readlines()
        return self.instructions
    
    def write_file(self):
        with open(self.instructions_file_path, 'w') as file:
            file.writelines(self.instructions)

    def write_to_file(self, instructions):
        with open(self.instructions_file_path, 'w') as file:
            file.writelines(instructions)

    def set_update_callback(self, callback):
        self._update_callback = callback

    def on_modified(self, event):
        if event.src_path == self.instructions_file_path:
            if self._update_callback is not None:
                self.read_file()
                self._update_callback(self.instructions)