#!/usr/bin/env python
# coding: utf-8

import geopy.distance


def shift_column(df, _from, _to, default=None):
    default = df[_from][0] if default is None else default

    df[_to] = df[_from]
    df[_to][1:-1], df[_to][0] = df[_to][2:], default
    return df


def t(df):
    return shift_column(df, _from='t0', _to='t1')


def latlon(df):
    df = shift_column(df, _from='lat0', _to='lat1', default=0)
    df = shift_column(df, _from='lon0', _to='lon1', default=0)
    return df
