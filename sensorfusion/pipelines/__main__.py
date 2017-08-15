#!/usr/bin/env python
# coding: utf-8
import os
import numpy as np
import pandas as pd

os.environ['DATA_DIR'] = '/home/ahmed/workspace/data/sensorlog'
os.environ['DATA_FILENAME'] = 'f5GX_G5eT1Y_20170814T174804.txt'

DATA_DIR, DATA_FILENAME = os.environ['DATA_DIR'], os.environ['DATA_FILENAME']
DATA_FILE = os.path.join(DATA_DIR, DATA_FILENAME)

from sensorfusion.pipelines import readers
from sensorfusion.pipelines import mechanics


def main():
    pd.DataFrame.drop = lambda this, columns: readers.clean(this, columns)
    pd.DataFrame.t = lambda this: mechanics.t(this)
    pd.DataFrame.latlon = lambda this: mechanics.latlon(this)
    pd.DataFrame.dt = lambda this: mechanics.dt(this)
    pd.DataFrame.dx = lambda this: mechanics.dx(this)
    pd.DataFrame.v = lambda this: mechanics.v(this)
    pd.DataFrame.normalize = lambda this: mechanics.normalize_nans(this)
    pd.DataFrame.summary = lambda this: this.agg({'v_kmh': ['max', 'min', 'average']})

    df = readers.sensor_data(DATA_FILE)

    df = df \
        .drop(columns=['_', 'alt']) \
        .t() \
        .latlon() \
        .dt() \
        .dx() \
        .v() \
        .normalize()

    print(df.summary())

    return


if __name__ == '__main__':
    main()
