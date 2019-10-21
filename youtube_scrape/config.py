import os
import yaml

"""This file loads in the settings.yaml into a python dictionary"""

with open('{}/settings.yaml'.format(os.path.dirname(os.path.realpath(__file__))), "r") as f:
    path = os.path.dirname(os.path.realpath(__file__))
    settings = yaml.load(f)

__version__ = '1.1.0'
__release_date__ = '10-20-2019'