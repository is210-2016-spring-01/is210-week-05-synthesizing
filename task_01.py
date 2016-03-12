#!/usr/bin/env/ python
# -*- coding: utf-8 -*-
"""A really good docstring for showing the date"""

import datetime
CURDATE = None
datetime.date.today()


def get_current_date():
    return CURDATE
    """This functions calculates the date.

    Args:
        None

    Return:
        str: Arguments concatenated with commas.

    Examples:
    >>> import task_01
    >>> print task_01.CURDATE
    None

    >>> task_01.get_current_date()
    datetime.date(2015, 1, 1)
    $ python -i task_01.py
    2015-01-01
    >>> CURDATE
    datetime.date(2015, 1, 1)
    """



