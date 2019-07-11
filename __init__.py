import sys
import os
from cuda_fmt import get_config_filename

sys.path.append(os.path.dirname(__file__))
from . import sqlparse

def opt():
    ini = get_config_filename('SQL Format')
    with open(ini) as f:
        text = f.read()
    return eval(text)

def do_format(text):
    return sqlparse.format(text, **opt() )
