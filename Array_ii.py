# This part consists of an application of linked lists: the sparse array. This is a form of array
# that conceptually consists of full sets of rows and columns, but only stores value in sparse
# entries. This is a form that guarantees the overall structure of the array, but saves a lot of
# space as it doesn't need the full memory space as a traditional array does.

# To define a sparse array, we need to separately define a linked list for storing row numbers,
# and another for storing columns and values.
# By definition, this form of array saves the space, but need extra time to iterate among rows and
# columns. This is another example of saving space by compensating time.
class ArrayRow:
    row_number = 0
    next_row = None
    # This will be the sentinel of a column
    row_sentinel = None

    def __init__(self, row_number=0, next_row=None, row_sentinel=None):
        self.row_number = row_number
        self.next_row = next_row
        self.row_sentinel = row_sentinel

    def set_next(self, next_row):
        self.next_row = next_row

    def set_sentinel(self, row_sentinel):
        self.row_sentinel = row_sentinel

    def get_sentinel(self):
        return self.row_sentinel

    def get_row_number(self):
        return self.row_number

    def get_next(self):
        return self.next_row


class ArrayEntry:
    column_number = 0,
    next_entry = None
    value = None

    def __init__(self, column_number=0, next_entry=None, value=None):
        self.column_number = column_number
        self.next_entry = next_entry
        self.value = value

    def set_next(self, next_entry):
        self.next_entry = next_entry

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def get_column_number(self):
        return self.column_number

    def get_next(self):
        return self.next_entry


# To operate such a list, it's best to first define methods for finding the row & column number
# of a value. This returns the node in linked list that locates before the target row.
def find_row_before(row, array_row_sentinel):
    array_row = array_row_sentinel
    while array_row.get_next() is not None and array_row.get_next().get_row_number() < row:
        array_row = array_row.get_next()
    return array_row


def find_column_before(column, row_sentinel):
    array_entry = row_sentinel
    while array_entry.get_next() is not None and array_entry.get_next().get_column_number() < column:
        array_entry = array_entry.get_next()
    return array_entry


# With the above two functions, it's easy to get a value according to row and column numbers.
def get_value(row, column, array_row_sentinel):
    array_row = find_row_before(row, array_row_sentinel).get_next()
    if array_row is None or array_row.get_row_number() > row:
        return None
    array_entry = find_column_before(column, array_row).get_next()
    if array_entry is None or array_entry.get_column_number() > column:
        return None
    return array_entry.get_value()


# The difference between getting a value and setting a value is that, the latter contains extending
# the array by inserting either a new row or column.
def set_value(sentinel, row, column, value):
    if value is None:
        pass
    array_row = find_row_before(row, sentinel)
    # if target row doesn't exist, create a new row.
    if array_row.get_next() is None or array_row.get_next().get_row_number() > row:
        new_row = ArrayRow()
        new_row.set_next(array_row.get_next())
        array_row.set_next(new_row)
        # define an entry (start) for columns
        sentinel_entry = ArrayEntry()
        new_row.set_sentinel(sentinel_entry)
    # operate the target row
    array_row = array_row.get_next()
    array_entry = find_column_before(column, array_row.get_sentinel())
    # if target entry doesn't exist, create a new entry.
    if array_entry.get_next() is None or array_entry.get_next().get_column_number() > column:
        new_entry = ArrayEntry()
        new_entry.set_next(array_entry.get_next())
        array_entry.set_next(new_entry)
    # operate the target column
    array_entry = array_entry.get_next()
    array_entry.set_value(value)


def delete_entry(sentinel, row, column):
    array_row = find_row_before(row, sentinel)
    # if target row doesn't exist, do nothing.
    if array_row.get_next() is None or array_row.get_next().get_row_number > row:
        pass
    target_row = array_row.get_next()
    array_entry = find_column_before(column, target_row.get_sentinel())
    # if target row doesn't exist, do nothing.
    if array_entry.get_next() is None or array_entry.get_next().get_column_number > column:
        pass
    array_entry.set_next(array_entry.get_next().get_next())
    if target_row.get_sentinel().get_next() is None:
        array_row.set_next(array_row.get_next().get_next())