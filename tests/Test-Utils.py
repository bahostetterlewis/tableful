from collections import OrderedDict
from collections import OrderedDict


def test_DictHeaders():
    '''Test that dictionaries are correctly turned into headers.'''
    import tableful_utils

    testDict = OrderedDict.fromkeys(['First', 'Second', 'Third'])
    expected = ('First', 'Second', 'Third')
    headers = tableful_utils._GetDictHeaders(testDict)
    assert expected == headers, \
        "Headers were {}, but should be {}".format(expected, headers)


def test_IterableListHeaders():
    '''Test that lists are correctly turned into headers.'''
    import tableful_utils
    testList = [('First', 'Second', 'Third')]
    expected = ('First', 'Second', 'Third')
    headers = tableful_utils._GetIterableHeaders(testList)
    assert expected == headers, \
        "Headers were {}, but should be {}".format(expected, headers)


def test_IterableTupleHeaders():
    '''Test that tuples are correctly turned into headers.'''
    import tableful_utils
    testTuple = (('First', 'Second', 'Third'),)
    expected = ('First', 'Second', 'Third')
    headers = tableful_utils._GetIterableHeaders(testTuple)
    assert expected == headers, \
        "Headers were {}, but should be {}".format(expected, headers)


def test_IterableHeadersFailNotIterable():
    '''Test that a non iterable returns no headers.'''
    import tableful_utils
    testInt = 3
    expected = None
    headers = tableful_utils._GetIterableHeaders(testInt)
    assert headers is expected, \
        "Headers were {} but should be None".format(headers)


def test_DictHeadersWhenNotDict():
    '''Test if DictHeaders only works for dicts.'''
    import tableful_utils
    testNonDict = ['First', 'Second', 'Third']
    expected = None
    headers = tableful_utils._GetDictHeaders(testNonDict)
    assert headers is expected, \
        "Headers were {} but should be None".format(headers)


def test_DictColumnToRowsWithDict():
    '''Test if _DictColumnsToRows returns rows correctly.'''
    import tableful_utils
    testDict = OrderedDict([
        ('First', [1, 2, 3]),
        ('Second', [4, 5, 6]),
        ('Third', [7, 8, 9])
     ])
    expected = ((1, 4, 7), (2, 5, 8), (3, 6, 9))
    rows = tableful_utils._GetDictRows(testDict)
    assert rows == expected, \
        "Rows were {} but should be {}".format(rows, expected)


def test_DictColumnToRowsWithNonDictList():
    '''Test if nondict returns None when given a list.'''
    import tableful_utils
    testList = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
    expected = None
    rows = tableful_utils._GetDictRows(testList)
    assert rows is expected, \
        "Rows were {} but should be None".format(rows, expected)


def test_DictColumnToRowsWithNonDictTuple():
    '''Test if nondict returns None when given a Tuple.'''
    import tableful_utils
    testTuple = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
    expected = None
    rows = tableful_utils._GetDictRows(testTuple)
    assert rows is expected, \
        "Rows were {} but should be None".format(rows, expected)


def test_IterableRowsHeadersInIterable():
    '''Test if rows are retrieved from non dict iterable when headers are in the iterable.'''
    import tableful_utils
    testList = [('First', 'Second', 'Third'), (1, 2, 3), (4, 5, 6), (7, 8, 9)]
    expected = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
    rows = tableful_utils._GetIterableRows(testList, embeddedHeaders=True)
    assert rows == expected, \
        "Rows were {} but should be {}".format(rows, expected)


def test_IterableRowsHeadersNotInIterable():
    '''Test if rows are retrieved from non dict iterable when headers are not in the iterable.'''
    import tableful_utils
    testList = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
    expected = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
    rows = tableful_utils._GetIterableRows(testList)
    assert rows == expected, \
        "Rows were {} but should be {}".format(rows, expected)


def test_IterableRowsWithDict():
    '''Test that when passed a dict the GetIterableRows function returns none.'''
    import tableful_utils
    testDict = {"First": [1, 2, 3], "Second": [4, 5, 6], "Third": [7, 8, 9]}
    expected = None
    rows = tableful_utils._GetIterableRows(testDict)
    assert rows == expected, \
        "Rows were {} but should be {}".format(rows, expected)


def test_IterableRowsWithDictAndBadEmbeddedHeadersFlag():
    '''Test that when passed a dict with embedded headers GetIterableRows returns none.'''
    import tableful_utils
    testDict = {"First": [1, 2, 3], "Second": [4, 5, 6], "Third": [7, 8, 9]}
    expected = None
    rows = tableful_utils._GetIterableRows(testDict, embeddedHeaders=True)
    assert rows == expected, \
        "Rows were {} but should be {}".format(rows, expected)


def test_IterableRowsWithNonIterable():
    '''
    Test that when given an non iterable, GetIterableRows returns none.
    '''
    import tableful_utils
    noniterable = int()
    expected = None
    rows = tableful_utils._GetIterableRows(noniterable)
    assert rows == expected, \
        "Rows were {} but should be {}".format(rows, expected)


def test_IterableRowsWithNonIterableAndBadEmbeddedFlagsTag():
    '''Test that when given a non iterable and embedded flags the GetIterableRows returns None.'''
    import tableful_utils
    noniterable = int()
    expected = None
    rows = tableful_utils._GetIterableRows(noniterable, embeddedHeaders=True)
    assert rows == expected, \
        "Rows were {} but should be {}".format(rows, expected)


def test_GetColumnWidthsHeadersLongest():
    '''Tests that _GetColumnWidths returns the header when it is longest part of the column.'''
    import tableful_utils
    headers = ("First", "Second")
    rows = ((1, 2), (3, 4))
    expected = (len(headers[0]), len(headers[1]))
    lengths = tableful_utils._GetColumnWidths(headers, rows)
    assert lengths == expected, \
        "Lengths were {} but should be {}".format(lengths, expected)


def test_GetColumnWidthsRowValueLongest():
    '''Tests that _GetColumnWidths returns the largest cell's length.'''
    import tableful_utils
    headers = ("F", "S")
    rows = ((1000, 2), (300, 4000))
    expected = (len(str(rows[0][0])), len(str(rows[1][1])))
    lengths = tableful_utils._GetColumnWidths(headers, rows)
    assert lengths == expected, \
        "Lengths were {} but should be {}".format(lengths, expected)


def test_BuildDivider():
    '''Tests that the divider is built to based on the size of the column widths.'''
    import tableful_utils
    columnWidths = (5, 4, 10)
    expected = "+-----+----+----------+"
    divider = tableful_utils._GetDivider(columnWidths)
    assert divider == expected, \
        "Divider was {} but should be {}".format(divider, expected)


def test_BuildCellStringSmallerThanCell():
    '''Tests that cells are properly padded with spaces when they are smaller than the width.'''
    import tableful_utils
    cellText = 123
    width = 5
    expected = " 123 "
    cell = tableful_utils._BuildCellString(cellText, width)
    assert cell == expected, \
        "Cell text was {} but should have been {}".format(cell, expected)

def test_BuildCellStringSameSizeAsCell():
    '''Tests that cells are properly padded with spaces when they are the same size as the width.'''
    import tableful_utils
    cellText = 12345
    width = 5
    expected = "12345"
    cell = tableful_utils._BuildCellString(cellText, width)
    assert cell == expected, \
        "Cell text was {} but should have been {}".format(cell, expected)
