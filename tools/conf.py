import os
import yaml

DIR_PATH = os.getcwd()
fp_config = DIR_PATH + "/tools/upgrade.yml"

def __import_config():
    with open(fp_config) as f:
        config = yaml.safe_load(f)
    return config
config = __import_config()