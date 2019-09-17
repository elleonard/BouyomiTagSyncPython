import yaml

CONFIG_FILE = "./config/config.yml"
class config:
  def __init__(self):
    with open(CONFIG_FILE, "r") as conf:
      self.settings = yaml.safe_load(conf)
  def get_sound_root(self):
    return self.settings['sound_root']
  def get_bouyomi_root(self):
    return self.settings['bouyomi_root']
  def get_bouyomi_replace_path(self):
    return self.get_bouyomi_root() + "\\ReplaceTag.dic"
