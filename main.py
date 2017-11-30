from queue import Queue
from threading import Thread
from PIL import Image
from icon import IconMgr
from common import keys
from state import State


def generate_lock_state(keys, state):
    width = 16
    height = 16
    image = Image.new('RGB', (width, height), (0, 0, 0))
    for i, key in enumerate(keys):
        if state & (2**i):
            sprite = Image.open(key['image'])
            image.paste(sprite, (8*i, 0))

    return image


def generate_images(keys):
    n_combinations = 2**len(keys)
    images = [generate_lock_state(keys, i) for i in range(n_combinations)]
    return images


icons = generate_images(keys)
Q = Queue()
stateMgr = State(Q)
mgr = IconMgr(Q, icons)
