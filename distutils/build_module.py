# coding=utf-8
import os
from glob import glob

os.system('python setup.py build')
os.system('copy '+glob('build/lib*/*.pyd')[0])
os.system('pause')