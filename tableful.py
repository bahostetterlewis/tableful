import tableful_utils
from functools import partial


def TablefulOfDict(dictionary, *, file=None):
    headers = tableful_utils._GetDictHeaders(dictionary)
    rows = tableful_utils._GetDictRows(dictionary)
    Tableful(rows, headers=headers, file=file)


def Tableful(iterable, *, headers=None, file=None):
    tableprinter = print
    embeddedHeaders = True if not headers else False

    if file is not None:
        tableprinter = partial(print, file=file)

    if not headers:
        headers = tableful_utils._GetIterableHeaders(iterable)

    if not headers:
        raise ValueError("No headers available")

    rows = tableful_utils._GetIterableRows(iterable, embeddedHeaders=embeddedHeaders)

    if not rows:
        raise ValueError("No rows available")

    columnWidths = tableful_utils._GetColumnWidths(headers, rows)
    divider = tableful_utils._GetDivider(columnWidths)
    tableprinter(divider)

    # create then print the header cells
    headerCells = []
    for header, width in zip(headers, columnWidths):
        headerCells.append(tableful_utils._BuildCellString(header, width))
    tableprinter("|{}|".format("|".join(headerCells)))
    tableprinter(divider)

    # create row cells then print them
    for row in rows:
        currentRow = []
        for cell, width in zip(row, columnWidths):
            currentRow.append(tableful_utils._BuildCellString(cell, width))
        tableprinter("|{}|".format("|".join(currentRow)))
    tableprinter(divider)
