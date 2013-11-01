import sublime, sublime_plugin

class JoinLinesCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for region in self.view.sel():
            line = self.view.full_line(region)
            to_delete = sublime.Region(region.begin(), line.end())
            self.view.erase(edit, to_delete)
