from itertools import zip_longest


def _GetDictHeaders(dictionary):
    '''
    Calculate headers for the table based on dict keys.

    Returns the headers as a tuple so that number of columns
    and their header can be determined.
    '''
    if isinstance(dictionary, dict):
        return tuple(key for key in dictionary)
    else:
        return None


def _GetIterableHeaders(iterable):
    '''
    Get headers out of an iterable.

    Headers are determined by the first item of the
    iterable. The first value must be an iterable.
    If the item isn't an iterable, it returns none.
    '''
    try:
        return tuple(iterable[0])
    except:
        return None


def _GetDictRows(dictionary):
    '''
    Grabs the columns out of a dict and turns them into rowss.
    '''
    try:
        values = (v for v in dictionary.values())
        columns = tuple(zip_longest(*values, fillvalue=''))
        return columns
    except AttributeError:
        return None


def _GetIterableRows(iterable, *, embeddedHeaders=False):
    '''
    Gets the rows from the iterable.
    '''
    if isinstance(iterable, dict):
        return None

    try:
        if embeddedHeaders:
            iterable = iterable[1:]
        return tuple(zip(*zip_longest(*iterable, fillvalue='')))  # by zipping we can ensure all cols are filled
    except:
        return None


def _GetColumnWidths(headers, rows):
    '''
    Calculate the width of each column.
    '''
    headers = (len(str(header)) for header in headers)
    columns = zip(*rows)
    columnLengths = []
    for column in columns:
        currentMax = max(column, key=lambda x: len(str(x)))
        columnLengths.append(len(str(currentMax)))  # convert to str so we can grab len
    return tuple(max(length) for length in zip(headers, columnLengths))


def _GetDivider(columMaxes, *, corners='+', divider='-'):
    '''
    Builds a divider based on the length of each column
    '''
    dashes = (divider * length for length in columMaxes)
    return "{0}{1}{0}".format(corners, corners.join(dashes))


def _BuildCellString(text, width):
    template = "{{: ^{}}}".format(width)
    return template.format(text)
