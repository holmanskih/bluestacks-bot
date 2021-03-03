import os
import yaml


class BlueStacksBot:
    cfg_key = ''
    cfg = None

    def read_cfg(self):
        raw_cfg = open("./config.yaml")
        self.cfg = yaml.load(raw_cfg, Loader=yaml.FullLoader)
        self.cfg_key = self.cfg['app']

        print(self.cfg)
        print(self.cfg['app'])

    # запускает программу bluestacks
    def run(self):
        os.system("open {0}".format(self.cfg[self.cfg_key]['path']))


if __name__ == '__main__':
    bot = BlueStacksBot()
    bot.read_cfg()
    bot.run()
