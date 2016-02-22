#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A module to return today's date."""

import datetime

CURDATE = None


def get_current_date():
    """Returns current date.

    Args:
        None

    Returns:
        date: Current date.

    Examples:
        >>> get_current_date()
        datetime.date(2016, 2, 22)
    """
    return datetime.date.today()

if __name__ == '__main__':
    CURDATE = get_current_date()
    print CURDATE
