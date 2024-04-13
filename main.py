from path import paths
import os

import time

v2ray = paths()['v2ray']
config = paths()['config']

os.system(f'{v2ray} -config={config}')

