from unittest import mock


def test_TablefulOfDict():
    '''
    Ensure that TablefulOfDict is calling Tableful with the propper values.

    Mocked tableful so that when it is called I can check what params were sent.
    '''
    import tableful
    from collections import OrderedDict
    testDict = OrderedDict([
        ('First', [1, 2, 3]),
        ('Second', [4, 5, 6]),
        ])
    tablefulHolder = tableful.Tableful
    tableful.Tableful = mock.MagicMock(name="Tableful")
    tableful.TablefulOfDict(testDict)
    mocked, tableful.Tableful = tableful.Tableful, tablefulHolder
    mocked.assert_called_with(
        ((1, 4), (2, 5), (3, 6)),
        headers=("First", "Second"),
        file=None,
        delim="default",
        )


def test_TablefulWithEmbeddedHeaders():
    '''Tests that a table is properly built with embedded headers.'''
    from io import StringIO
    import tableful
    iterable = (("First", "Second"), (1, 3), (2, 4))
    expected = ('+-----+------+',
                '|First|Second|',
                '+-----+------+',
                '|  1  |  3   |',
                '|  2  |  4   |',
                '+-----+------+')
    expected = '\n'.join(expected)
    actual = StringIO("")
    tableful.Tableful(iterable, file=actual)
    assert actual.getvalue().strip() == expected.strip(), \
        "Table was\n{}\nBut should be\n{}".format(actual.getvalue().strip(), expected.strip())


def test_TablefulWithNoEmbeddedHeaders():
    '''Tests that a table is properly built with no embedded headers.'''
    from io import StringIO
    import tableful
    iterable = ((1, 3), (2, 4))
    headers = ("First", "Second")
    expected = ('+-----+------+',
                '|First|Second|',
                '+-----+------+',
                '|  1  |  3   |',
                '|  2  |  4   |',
                '+-----+------+')
    expected = '\n'.join(expected)
    actual = StringIO("")
    tableful.Tableful(iterable, file=actual, headers=headers)
    assert actual.getvalue().strip() == expected.strip(), \
        "Table was\n{}\nBut should be\n{}".format(actual.getvalue().strip(), expected.strip())
