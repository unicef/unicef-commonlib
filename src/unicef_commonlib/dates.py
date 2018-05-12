# -*- coding: utf-8 -*-
from datetime import datetime


def get_quarter(retrieve_date=None):
    if not retrieve_date:
        retrieve_date = datetime.today()
    month = retrieve_date.month
    return "q%s" % ((month // 3) + 1)
