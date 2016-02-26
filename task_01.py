#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module gets the current date & checks if code run direct or imported."""

import datetime

CURDATE = None


def get_current_date():
    """A function to get the current day and return as date var.

    Args:
        None.

    Returns:
        str: The current date formatted as YYYY, M, D.

    Examples:

        >>> get_current_date()
        datetime.date(2016, 2, 22)

        >>> get_current_date()
        datetime.date(2016, 2, 29)
    """
    global date

    return datetime.date.today()

if __name__ == '__main__':
    CURDATE = get_current_date()
    print CURDATE
