FILEPATH = "todo.txt"


def get_todos(filepath = FILEPATH):
    """
    reads the file and returns item list from the file
    :param filepath:
    :return:
    """
    with open(filepath, "r") as file_read:
        todos_local = file_read.readlines()
    return todos_local


def get_write_todos(filepath, todo_write):
    """
    writes new todo items to list, this does not return any value.
    :param filepath:
    :param todo_write:
    :return:
    """
    with open(filepath, 'w') as file:
        file.writelines(todo_write)


def truncate(filename='todo.txt'):
    """
    This functions deletes all items in the file
    :param filename:
    :return:
    """
    file = open(filename, 'r+')
    file.truncate(0)
    file.close()

