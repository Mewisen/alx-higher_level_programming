#!/usr/bin/python3
"""
<<<<<<< HEAD

Module composed by a function that prints 2 new lines after ".?:" characters

"""


def text_indentation(text):
    """ Function that prints 2 new lines after ".?:" characters

    Args:
        text: input string

    Returns:
        No return

    Raises:
        TypeError: If text is not a string


    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    s = text[:]

=======
Module composed by a function that prints 2 new lines after "?:" characters
"""

def text_indentation(text):
    """ Function that prints 2 new lines after "?:" characters
    Args:
        text: input string
    Returns:
        No return
    Raises:
        TypeError: if text is not a string
    """

    if type(text) is not str:
        raise TypeError("text must be an string")

    s = text[:]
>>>>>>> e9d83ad4a58936e721bd23ba1abf69aeec7567a7
    for d in ".?:":
        list_text = s.split(d)
        s = ""
        for i in list_text:
            i = i.strip(" ")
            s = i + d if s is "" else s + "\n\n" + i + d
<<<<<<< HEAD

=======
>>>>>>> e9d83ad4a58936e721bd23ba1abf69aeec7567a7
    print(s[:-3], end="")
