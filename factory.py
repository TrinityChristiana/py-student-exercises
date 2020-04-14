from collections import namedtuple

def class_maker(class_name, fields, last_defaults = []):
    """Shorthand-way to initiate Class

    Keyword arguments:

    class_name -- Name of class

    fields -- iteriable for class properties 

    last_defaults -- Defaults for properties starting from right to left.

    Returns: namedtuple
    """

    new_list = list(map(lambda foo: None, fields))

    default_index = len(last_defaults)

    for i in range(default_index):
        new_list[-(i + 1)] = last_defaults[-(i + 1)]

    return namedtuple(class_name, fields, defaults=new_list)
