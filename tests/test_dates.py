from datetime import datetime

from freezegun import freeze_time

import pytest

from unicef_commonlib.dates import get_quarter

params = [('1/Jan/10', 'q1'),  # jan, feb, marc
          ('1/Apr/10', 'q2'),  # apr, may, jun
          ('1/Jul/10', 'q3'),  # jul, aug, sep
          ('1/Oct/10', 'q4'),  # oct, nov, dec
          (None, 'q4')]


@pytest.mark.parametrize("dt", params,
                         ids=[str(a[0]) for a in params])
@freeze_time("1955-Nov-12")
def test_get_quarter(dt):
    date, expected = dt
    assert get_quarter(date and datetime.strptime(date, '%d/%b/%y')) == expected
