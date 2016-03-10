#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This is the week 5 synthesizing task to use the datetime module"""

import datetime


def get_current_date():
    """ provide the current date in datetime.date formate

    Args: NONE

    Returns:
        date: date formate of the current date.

    Exampled:

        >>> get_current_date()
        date(2016, 2, 26)

    """

    return datetime.date.today()

if __name__ == "__main__":
    CURDATE = get_current_date()
    print CURDATE
else:
    CURDATE = None
