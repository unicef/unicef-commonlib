import pytest
from unittest import TestCase

from unicef_commonlib.reflect import fqn

params = ((list, 'builtins.list'),
          ('abc', 'abc'),
          (TestCase(), 'unittest.case.TestCase'),
          (int, 'builtins.int'),
          )


@pytest.mark.parametrize("arg", params, ids=[p[1] for p in params])
def test_fqn(arg):
    target, expected = arg
    assert fqn(target) == expected


def test_fqn_error():
    with pytest.raises(ValueError):
        assert fqn(None) == ''
