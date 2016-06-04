#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A small docstring for a new module"""


import datetime

CURDATE = None


def get_current_date():
    """Does some function and resturns a date.

    Args:
        Runs function through a return and call statement

    Returns:
        int: Retrieves the current date

    Examples:

        >>> get_current_date()
        'datetime.date(2016, 2, 28)'
    """
    return datetime.date.today()
datetime.date.today()

if __name__ == '__main__':
    CURDATE = get_current_date()
    print CURDATE
