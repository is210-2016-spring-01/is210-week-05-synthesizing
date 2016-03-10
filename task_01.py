#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module returns the current date and time"""

import datetime

CURDATE = None


def get_current_date():
    """Defines a function that provides the current date

    Args:
    None

    Returns:
    Date Object: Current date

    Example:
    >>> task_01.get_current_date()
    datetime.date(2016, 2, 25)
    """

    return datetime.date.today()

if __name__ == "__main__":
    CURDATE = get_current_date()
    print CURDATE
