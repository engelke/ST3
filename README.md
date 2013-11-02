ST3
===

Customized behaviors for Sublime Text 3

Sublime Text lacks very many line-oriented editing
commands. These functions add some, inspired by the Brief text editor.

Install these Python programs into your Packages folder
to enable new functions. You can then map keystrokes to the
functions as shown in the sample Windows keymap file. Those
recommended key mappings are shown *(in parentheses)*.

### `delete_line.py` *(ALT-D)*

Delete the current line, or all the lines containing the
current selection, if there is one.

### `delete_to_end_of_line.py` *(ALT-K)*

Delete from the cursor to the end of the line. Deletes
the current selection, too, if there is one.

### `insert_line.py` *(CTRL-V)*

Checks to see if the clipboard contains a complete final
line (ends with a newline). If so, pastes the selection
above the current line, instead of at the cursor.

### `join_lines.py` *(ATL-J)*

Joins the current line with the next line, eliminating
leading whitespace on the next line when doing so.
