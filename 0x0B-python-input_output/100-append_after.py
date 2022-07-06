#!/usr/bin/python3
""" Module : 100-append_after"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a line of text to a file, after each line containing a
    specific string."""

    text = ""
    with open(filename, encoding='utf-8') as myFile:
        for line in myFile:
            text += line
            if search_string in line:
                text += new_string

    with open(filename, 'w', encoding='utf-8') as myFile:
        myFile.write(text)
