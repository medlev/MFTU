# -*- coding: utf-8 -*-
#example 1 вывод текущего времени "секунды"
from datetime import datetime
def get_seconds():
    """Return current seconds"""
    return datetime.now().second
print(get_seconds())
