import sublime, sublime_plugin

class DeleteToEndOfLineCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for region in self.view.sel():
            line = self.view.line(region)
            to_delete = sublime.Region(region.begin(), line.end())
            self.view.erase(edit, to_delete)
