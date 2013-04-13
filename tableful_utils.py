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


def _GetDictColumns(dictionary):
    '''
    Grabs the columns out of a dict and turns them into rowss.
    '''
    try:
        values = (v for v in dictionary.values())
        columns = tuple(zip(*values))
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
        return tuple(iterable)
    except:
        return None
