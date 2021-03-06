# -*- coding: utf-8 -*-

from decimal import Decimal
from datetime import datetime
import dateutil.parser as parser_dateutil

from unicodedata import normalize

def normalize_str(string):
    """
    Remove special characters and return the ascii string
    """
    if string:
        if not isinstance(string, unicode):
            string = unicode(string, 'utf-8', 'replace')

        string = string.encode('utf-8')

        return normalize('NFKD', string.decode('utf-8')).encode('ASCII','ignore')

    return ''

def format_percent(value):
    if value:
        return Decimal(value) / 100

def format_datetime(value):
    """
    Format datetime
    """
    dt_format = '%Y-%m-%dT%H:%M:%I'
    if isinstance(value, datetime):
        return value.strftime(dt_format)

    try:
        value = parser_dateutil.parse(value).strftime(dt_format)
    except AttributeError:
        pass

    return value
