#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 01 Week 05"""

import datetime

CURDATE = None

def get_current_date():
    """Return current day as date object
    Args: Empty
    
    Returns:
        date: 
    Example:
        >>> get_current_date()
        datetime.date(2016, 29, 8)"""
    return datetime.date.today()


if __name__ == '__main__':
    CURDATE = get_current_date()
    print CURDATE
