#!/usr/bin/env python
# -*- coding: utf-8 -*-
# wwq @ 2013-11-11 10:50:39

import time

def ch_time(f_time):
    '''转换时间格式
    '''
    _f = f_time.strftime("%Y-%m-%d %H:%M")
    result = time.strptime(_f, "%Y-%m-%d %H:%M")

    return result
