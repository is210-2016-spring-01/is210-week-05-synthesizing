#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Doing things with datetime"""

import datetime

CURDATE = None

def get_current_date():
    """this function returns the date.

    Args:
        Takes no parameters!

    Returns:
        date: today's date

    Examples:
    
        >>> import task_01
        >>> print task_01.CURDATE
        None

        >>> task_01.get_current_date()
        datetime.date(2015, 1, 1)
    """  
    date = datetime.date.today()
    return date
