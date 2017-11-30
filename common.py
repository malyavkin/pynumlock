from PIL import Image

VK_CAPITAL = 0x14
VK_NUMLOCK = 0x90
KEYS = [
    {
        'keycode': VK_CAPITAL,
        'image': 'images/caps.png'
    },{
        'keycode': VK_NUMLOCK,
        'image': 'images/num.png'
    }
]



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


icons = generate_images(KEYS)
