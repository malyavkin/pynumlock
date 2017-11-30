import ctypes
import threading

from common import keys

user32 = ctypes.WinDLL("User32.dll")


class State:
    def __init__(self, queue):
        self.q = queue
        self.thread = threading.Thread(target=self.watcher)
        self.thread.start()

    def watcher(self):
        old_state = -1
        while True:
            new_state = State.get_locks_state()
            if old_state != new_state:
                self.q.put(new_state)
            old_state = new_state

    @staticmethod
    def get_locks_state():
        status = 0
        for i, key in enumerate(keys):
            status |= (1 if user32.GetKeyState(key['keycode']) else 0) << i
        return status
