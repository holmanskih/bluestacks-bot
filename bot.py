import os

import yaml
import pyautogui
from pynput.mouse import Button, Controller


# run bluestacks
# open game
# get daily bonus
# close the game
# enter settings
# enter settings clock and time
# update time
# open game
class BlueStacksBot:
    cfg_key = ''
    cfg = None

    def __init__(self):
        screen_width, screen_height = pyautogui.size()

        current_mouse_x, current_mouse_y = pyautogui.position()
        print(screen_width, screen_height)
        print(current_mouse_x, current_mouse_y)

    def read_cfg(self):
        raw_cfg = open("./config.yaml")
        self.cfg = yaml.load(raw_cfg, Loader=yaml.FullLoader)
        self.cfg_key = self.cfg['app']

        print(self.cfg)
        print(self.cfg['app'])

    # запускает программу bluestacks
    def run(self):
        os.system("open {0}".format(self.cfg[self.cfg_key]['path']))

    def move_mouse(self, x, y):
        pyautogui.moveTo(x, y)

    def double_click(self, x, y):
        pyautogui.doubleClick(x, y)

    def single_click(self):
        pyautogui.click()

    def do_actions(self):
        for action in self.cfg['actions']:

            # log our action
            print("Current action: {0}".format(action['name']))

            action_type = action['type']
            x = action['x']
            y = action['y']

            # do mouse click
            if action_type == "double_click":
                mouse = Controller()
                pyautogui.moveTo(x, y)
                mouse.click(Button.left)

            elif action_type == "single_click":
                self.single_click()


def track_live_mouse_position():
    while True:
        current_mouse_x, current_mouse_y = pyautogui.position()
        print(current_mouse_x, current_mouse_y)


if __name__ == '__main__':
    # track_live_mouse_position()
    bot = BlueStacksBot()
    bot.read_cfg()
    bot.do_actions()
    # bot.run()

