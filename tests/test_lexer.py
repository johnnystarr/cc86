#!/usr/bin/env python

import pytest

from cc86.lexer import Lexer


@pytest.fixture()
def lexer():
    lexer = Lexer()
    yield lexer


def test_lexer_new(lexer):
    assert lexer.current_char_count == 1
    assert lexer.current_line_number == 1


