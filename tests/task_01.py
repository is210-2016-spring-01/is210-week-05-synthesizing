#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This is the module that assigns the current date. """


import datetime


CURDATE = None


def get_current_date():
    """Function gets current date

    Args:
        None

    Returns:
        Date Object: Returns current date.

    Examples:

        >>> get_current_date()
        datetime.date(2016, 2, 24)
    """
    return datetime.date.today()

if __name__ == '__main__':
    CURDATE = get_current_date()
    print CURDATE
