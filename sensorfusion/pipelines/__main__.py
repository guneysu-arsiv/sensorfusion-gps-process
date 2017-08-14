#!/usr/bin/env python
# coding: utf-8
import os

os.environ['DATA_DIR'] = '/home/ahmed/workspace/data/sensorlog'
os.environ['DATA_FILENAME'] = 'f5GX_G5eT1Y_20170814T174804.txt'

DATA_DIR, DATA_FILENAME = os.environ['DATA_DIR'], os.environ['DATA_FILENAME']
DATA_FILE = os.path.join(DATA_DIR, DATA_FILENAME)


from sensorfusion.pipelines import readers
from sensorfusion.pipelines import mechanics

def main():
    df = readers.sensor_data(DATA_FILE)
    df = readers.clean(df,['_', 'alt'])
    df = mechanics.t(df)
    df = mechanics.latlon(df)

    print(df.head(3))
    # print(df.info())
    return


if __name__ == '__main__':
    main()
