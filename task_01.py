#!usr/bin/env python
# -*- coding: utf-8 -*-
""" Using the datetime import"""

import datetime

CURDATE = None


def get_current_date():
    """ Using date and time to get current time
    Arg:
        No defined argument

    Return:
    (   mixed): lists date time and what day today is.

    example:
        >>> task_01.get_current_date()
        datetime.date(2015, 1, 1)
    """
    return datetime.date.today()
