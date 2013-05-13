import tableful_utils
from collections import namedtuple
from functools import partial

_delimiter = namedtuple('delimiter', ['outer_left',
                                      'inbetween',
                                      'outer_right',
                                      'outer_header_left',
                                      'header_inbetween',
                                      'outer_header_right',
                                      'corners',
                                      'divider',
                                      'before_all',
                                      'after_all'
                                      ])
_delimiter_values = {
    "default": _delimiter('|', '|', '|', '|', '|', '|',  corners='+', divider='-', before_all='', after_all=''),
    "html": _delimiter(outer_left='<tr><td class="tablefuletd" align="center">',
                       inbetween='</td><td class="tablefultd" align="center">',
                       outer_right='</td></tr>',
                       outer_header_left='<tr><th class="tablefulth" align="center">',
                       header_inbetween='</th><th class="tablefulth" align="center">',
                       outer_header_right='</th></tr>',
                       corners='',
                       divider='',
                       before_all='<table border="1" class="tableful">',
                       after_all='</table>'
                       )
}


def TablefulOfDict(dictionary, *, file=None, delim="default"):
    '''
    Prints a dict in a tableful way!

    keyword args:
    file - any object that can be written to
    delim - set to html for an html table
            see docs of Tableful for custom delim settings which are passed through here
    '''
    headers = tableful_utils._GetDictHeaders(dictionary)
    rows = tableful_utils._GetDictRows(dictionary)
    Tableful(rows, headers=headers, file=file, delim=delim)


def Tableful(iterable, *, headers=None, file=None, delim="default"):
    '''
    Prints an iterable in a tableful way!

    keyword args:
    headers - an optional headers iterable that will be used in place of main iterables
    file - any object that can be written to
    delim - two value types are excepted
        1) default - creates the default table using +, |, and - to draw everything
        2) html - creates a table with class tableful and td class tablefultd and th has class tablefulth
                  The th are centered
                  The td are centered
                  table has border=1
                  The classes allow for overiding these settings in css
        3) a dictionary that has the following keywords to create a custom table
                - outer_left: what will appear on the outer most left side of rows default is |
                - inbetween: seperates each cell from the one next to it in the rows and headers, default is |
                - outer_right: same as outer_left but on the very outer right edge of the table  default is |
                - outer_header_left: similar to outer_left only changes the headers outer most delim default is |
                - header_inbetween: simlar to inbetween, appears between each header cell defaults is |
                - outer_header_right: similar to outer_header_right but on the right side default is |
                - corners: appears on all corners, and between cell dividers default is +
                - divider: creates the divider for the top, after header, and bottom of table
                    combined with corners default is -
                - before_all: printed before the table default is blank, used for things like <table> tag
                - after_all: printed after the whole table default is blank, used for things like a </table> tag
    '''
    try:
        delimiters = _delimiter_values[delim]
    except KeyError:
        delimiters = _delimiter(**delim)

    tableprinter = print
    embeddedHeaders = True if not headers else False

    if file is not None:
        tableprinter = partial(tableprinter, file=file)

    if not headers:
        headers = tableful_utils._GetIterableHeaders(iterable)

    if not headers:
        raise ValueError("No headers available")

    rows = tableful_utils._GetIterableRows(iterable, embeddedHeaders=embeddedHeaders)

    if not rows:
        raise ValueError("No rows available")

    columnWidths = tableful_utils._GetColumnWidths(headers, rows)
    divider = tableful_utils._GetDivider(columnWidths, corners=delimiters.corners, divider=delimiters.divider)

    tableprinter(delimiters.before_all)
    tableprinter(divider)
    # create then print the header cells
    headerCells = []
    for header, width in zip(headers, columnWidths):
        headerCells.append(tableful_utils._BuildCellString(header, width))
    tableprinter("{}{}{}".format(delimiters.outer_header_left, delimiters.header_inbetween.join(headerCells), delimiters.outer_header_right))
    tableprinter(divider)

    # create row cells then print them
    for row in rows:
        currentRow = []
        for cell, width in zip(row, columnWidths):
            currentRow.append(tableful_utils._BuildCellString(cell, width))
        tableprinter("{}{}{}".format(delimiters.outer_left, delimiters.inbetween.join(currentRow), delimiters.outer_right))
    tableprinter(divider)
    tableprinter(delimiters.after_all)
