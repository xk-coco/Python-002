#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/2 23:19
# @File    : CustomExceptionClass.py

class DbConnectionError(Exception):
    """先当固定的用法记着"""

    def __init__(self, info):
        super(DbConnectionError, self).__init__(info)
        self._info = info

    def __str__(self):
        return self._info
