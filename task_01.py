#!/usr/bin/env python
# _*_ coding: utf-8 _*_
"""Task 1 file."""

import datetime

CURDATE = None


def get_current_date():
    """Getting current date.

    Args:

    Returns:
        date: returns current date.

    Examples:

        >>> get_currrent_date()
        'datetime.date(2016, 2, 28)'
    """
    date = datetime.date.today()
    return date


CURDATE = get_current_date()

print CURDATE
