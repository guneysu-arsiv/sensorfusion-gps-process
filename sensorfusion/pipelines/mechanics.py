#!/usr/bin/env python
# coding: utf-8

import geopy.distance
import numpy
import pandas as pd


def shift_column(df, _from, _to, default=None):
    default = df[_from][0] if default is None else default
    df[_to] = df[_from]
    df[_to][1:-1], df[_to][0] = df[_to][2:], default
    return df


def t(df):
    return shift_column(df, _from='t0', _to='t1', default=df['t0'][1])


def dt(df):
    df['dt'] = df.t1 - df.t0
    return df


def distance(lat0, lon0, lat1, lon1):
    return geopy.distance.vincenty(
        (lat1, lon1),
        (lat0, lon0)
    ).meters


def dx(df):
    df['dx'] = tuple(map(lambda a, b, c, d: distance(a, b, c, d), df['lat0'], df['lon0'], df['lat1'], df['lon1']))
    return df


def v(df):
    df['v_ms'] = 1000.0 * df['dx'] / df['dt']
    df['v_kmh'] = 3.6 * df['v_ms']
    return df


def latlon(df):
    df = shift_column(df, _from='lat0', _to='lat1', default=df['lat0'][0])
    df = shift_column(df, _from='lon0', _to='lon1', default=df['lon0'][0])
    return df


def normalize_nans(df):
    df = df[numpy.isfinite(df['v_kmh'])]
    df = df[numpy.isfinite(df['v_ms'])]
    return df