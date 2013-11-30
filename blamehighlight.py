import os
from subprocess import Popen, PIPE
import sublime, sublime_plugin

def get_stdout_string(command):
	p = Popen(command, stdout=PIPE, stderr=PIPE)
	output = p.stdout.read().decode("utf-8")
	return output

def extract_user_lines(directory, fileName, email):
	os.chdir(directory)
	email = "<%s>" % email
	output = get_stdout_string(["git", "blame", "--line-porcelain", fileName])

	lines = output.splitlines()

	accumulator = []
	realLines = []

	for line in lines:
		lineParts = line.split(" ")
		if len(lineParts) < 2:
			continue

		if len(lineParts) == 4 or len(lineParts) == 3:
			if len(lineParts[0]) == 40 and lineParts[1].isdigit() and lineParts[2].isdigit():
				accumulator.append(int(lineParts[2]))

		if lineParts[0] == "author-mail":
			if lineParts[1] == email:
				realLines.extend(accumulator)
			accumulator = []

	return realLines


class SeeMyCode(sublime_plugin.TextCommand):
	def highlight_lines(self, lineList):
		view = self.view
		highlighted_regions = []
		for lineNum in lineList:
			linePoint = view.text_point(lineNum - 1, 0)
			lineRegion = view.line(linePoint)
			highlighted_regions.append(lineRegion)

		view.add_regions('blameGutter', highlighted_regions, "string", "dot", sublime.DRAW_NO_FILL | sublime.DRAW_NO_OUTLINE)

	def run(self, edit):
		self.settings = sublime.load_settings("BlameHighlight.sublime-settings")
		fileName = self.view.file_name ()
		dirName = os.path.dirname(fileName)
		os.chdir(dirName)
		if os.system("git rev-parse") == 0:
			email = get_stdout_string(["git", "config", "user.email"])
			email = email.splitlines()
			email = email[0]
			gitLines = extract_user_lines(dirName, fileName, email)
			self.highlight_lines(gitLines)

class ClearBlameHighlights(sublime_plugin.TextCommand):
	def run(self, edit):
		self.view.erase_regions('blameGutter')



