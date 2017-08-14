#!/usr/bin/env python
# coding: utf-8

import pandas as pd


def sensor_data(filepath):
    """
    reads from sensor fusion text file containing gps only data
    :param filepath:
    :return:
    """
    df = pd.read_csv(
        filepath_or_buffer=filepath,
        delimiter='\t',
        names=['t0', '_', 'lat0', 'lon0', 'alt'],
        header=None,
    )
    return df


def clean(df, columns=['_']):
    """
    cleans _ column from data frame
    :param df:
    :return:
    """
    for col in columns:
        del df[col]

    return df
