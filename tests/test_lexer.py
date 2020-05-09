#!/usr/bin/env python

import pytest

from cc86.lexer import Lexer


@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """


def test_lexer_new():
    lex = Lexer()
    assert lex.current_char_count == 1

