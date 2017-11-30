import pystray


class IconMgr:
    def __init__(self, queue, icons):
        self.q = queue
        self.icons = icons
        icon = pystray.Icon('icon')
        icon.run(self.setup)

    def setup(self, icon):

        while True:
            image = self.q.get()
            if image == -1:
                icon.stop()
                break
            icon.icon = self.icons[image]
            icon.visible = True





