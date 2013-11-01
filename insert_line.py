import sublime, sublime_plugin

class InsertLinesCommand(sublime_plugin.TextCommand):
    """
    If the clipboard contains an entire line, paste
    it above the current line instead of at the cursor.
    """

    def run(self, edit):
        clipped = sublime.get_clipboard()
        if clipped[-1] != '\n':
            self.view.run_command('paste')
        else:
            for region in self.view.sel():
                if region.empty():
                    line = self.view.line(region)
                    self.view.insert(edit, line.begin(), clipped)
