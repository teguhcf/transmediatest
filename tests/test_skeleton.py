#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from kumparan_test.skeleton import fib

__author__ = "teguhcf"
__copyright__ = "teguhcf"
__license__ = "mit"


def test_fib():
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(7) == 13
    with pytest.raises(AssertionError):
        fib(-10)
