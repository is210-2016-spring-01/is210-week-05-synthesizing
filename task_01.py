#!/usr/bin/env/python
# -*- coding: utf-8 -*-
"""Using the datetime module."""


import datetime

CURDATE = None


def get_current_date():
    """Getting the current date.

    Args:
        no parameters(mixed): Doesn't take any parameters

    Returns:
        date: The current date

    Example:

    >>>import task_01
    >>>task_01.get_current_date()
    datetime.date(2015, 1, 1)
    """
    return datetime.date.today()

if __name__ == '__main__':
    CURDATE = get_current_date()
    print CURDATE
