def test_DictHeaders():
    '''
    Test that dictionaries are correctly turned into headers.
    '''
    import tableful_utils
    from collections import OrderedDict

    testDict = OrderedDict.fromkeys(['First', 'Second', 'Third'])
    expected = ('First', 'Second', 'Third')
    headers = tableful_utils._GetDictHeaders(testDict)
    assert expected == headers, \
        "Headers were {}, but should be {}".format(expected, headers)


def test_IterableListHeaders():
    '''
    Test that lists are correctly turned into headers.
    '''
    import tableful_utils
    testList = [('First', 'Second', 'Third')]
    expected = ('First', 'Second', 'Third')
    headers = tableful_utils._GetIterableHeaders(testList)
    assert expected == headers, \
        "Headers were {}, but should be {}".format(expected, headers)


def test_IterableTupleHeaders():
    '''
    Test that tuples are correctly turned into headers.
    '''
    import tableful_utils
    testTuple = (('First', 'Second', 'Third'),)
    expected = ('First', 'Second', 'Third')
    headers = tableful_utils._GetIterableHeaders(testTuple)
    assert expected == headers, \
        "Headers were {}, but should be {}".format(expected, headers)


def test_IterableHeadersFailNotIterable():
    '''
    Test that a non iterable returns no headers.
    '''
    import tableful_utils
    testInt = 3
    expected = None
    headers = tableful_utils._GetIterableHeaders(testInt)
    assert headers is expected, \
        "Headers were {} but should be None".format(headers)


def test_DictHeadersWhenNotDict():
    '''
    Test if DictHeaders only works for dicts.
    '''
    import tableful_utils
    testNonDict = ['First', 'Second', 'Third']
    expected = None
    headers = tableful_utils._GetDictHeaders(testNonDict)
    assert headers is expected, \
        "Headers were {} but should be None".format(headers)


def test_DictColumnToRowsWithDict():
    '''
    Test if _DictColumnsToRows returns rows correctly.
    '''
    import tableful_utils
    from collections import OrderedDict
    testDict = OrderedDict([
        ('First', [1, 2, 3]),
        ('Second', [4, 5, 6]),
        ('Third', [7, 8, 9])
     ])
    expected = ((1, 4, 7), (2, 5, 8), (3, 6, 9))
    rows = tableful_utils._GetDictColumns(testDict)
    assert rows == expected, \
        "Rows were {} but should be {}".format(rows, expected)


def test_DictColumnToRowsWithNonDictList():
    '''
    Test if nondict returns None when given a list.
    '''
    import tableful_utils
    testList = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
    expected = None
    rows = tableful_utils._GetDictColumns(testList)
    assert rows is expected, \
        "Rows were {} but should be None".format(rows, expected)


def test_DictColumnToRowsWithNonDictTuple():
    '''
    Test if nondict returns None when given a Tuple.
    '''
    import tableful_utils
    testTuple = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
    expected = None
    rows = tableful_utils._GetDictColumns(testTuple)
    assert rows is expected, \
        "Rows were {} but should be None".format(rows, expected)


def test_IterableRowsHeadersInIterable():
    '''
    Test if rows are retrieved from non dict iterable when headers are in the iterable.
    '''
    import tableful_utils
    testList = [('First', 'Second', 'Third'), (1, 2, 3), (4, 5, 6), (7, 8, 9)]
    expected = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
    rows = tableful_utils._GetIterableRows(testList, embeddedHeaders=True)
    assert rows == expected, \
        "Rows were {} but should be {}".format(rows, expected)


def test_IterableRowsHeadersNotInIterable():
    '''
    Test if rows are retrieved from non dict iterable when headers are not in the iterable.
    '''
    import tableful_utils
    testList = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
    expected = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
    rows = tableful_utils._GetIterableRows(testList)
    assert rows == expected, \
        "Rows were {} but should be {}".format(rows, expected)


def test_IterableRowsWithDict():
    import tableful_utils
    testDict = {"First": [1, 2, 3], "Second": [4, 5, 6], "Third": [7, 8, 9]}
    expected = None
    rows = tableful_utils._GetIterableRows(testDict)
    assert rows == expected, \
        "Rows were {} but should be {}".format(rows, expected)


def test_IterableRowsWithDictAndBadEmbeddedHeadersFlag():
    import tableful_utils
    testDict = {"First": [1, 2, 3], "Second": [4, 5, 6], "Third": [7, 8, 9]}
    expected = None
    rows = tableful_utils._GetIterableRows(testDict, embeddedHeaders=True)
    assert rows == expected, \
        "Rows were {} but should be {}".format(rows, expected)


def test_IterableRowsWithNonIterable():
    import tableful_utils
    noniterable = int()
    expected = None
    rows = tableful_utils._GetIterableRows(noniterable)
    assert rows == expected, \
        "Rows were {} but should be {}".format(rows, expected)


def test_IterableRowsWithNonIterableAndBadEmbeddedFlagsTag():
    import tableful_utils
    noniterable = int()
    expected = None
    rows = tableful_utils._GetIterableRows(noniterable, embeddedHeaders=True)
    assert rows == expected, \
        "Rows were {} but should be {}".format(rows, expected)
