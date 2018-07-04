# -*- coding: utf-8 -*-
"""
simplize UTC time and local-time conversion
"""
import pytz
from datetime import datetime, timezone

def utctime():
    return datetime.now(timezone.utc)

time = utctime

def localtime(tz=pytz.timezone('Asia/Shanghai')):
    return datetime.now(tz)

def mkdatetime(year, month, day, hour=0, minute=0, second=0, microsecond=0, tzinfo=None, *, fold=0):
    dt = datetime(year, month, day,
                  hour, minute, second, microsecond,
                  fold=fold)
    return dt.astimezone(tzinfo)
