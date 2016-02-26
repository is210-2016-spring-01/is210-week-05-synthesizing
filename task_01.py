#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This file will return today's date"""

import datetime

CURDATE = None


def get_current_date():
    """Returns today's date.

    Args:
        (): No argumentss

    Returns:
        Date (mixed): returns the actual day's date.

    Examples:

        >>> CURDATE
        datetime.date(2016, 2, 26)

    """
    date = datetime.date.today()
    return date

if __name__ == "__main__":
    CURDATE = get_current_date()
    print CURDATE
