BlameHighlighter
================

### What does it do?

This Sublime Text 3 Extension highlights the code in a file that is previously committed by you. It does this by using [git-blame](https://www.kernel.org/pub/software/scm/git/docs/git-blame.html) which shows which lines were committed by you.

![Screenshot](http://imgur.com/EvAxQRx.png)

### Why would it be useful?

If you have previously committed a small bit of code in a large file, you can quickly find that section because it gets highlighted on the minimap.

### How to use it?

Invoke the command pane (Ctrl + Shift + P or Cmd + Shift + P) and run the following functions:

* `BlameHighlighter: Highlight the code you have edited` - to highlight the changes.
* `BlameHighlighter: Clear Highlighted Blames` - to clear the highlights

### License

This is licensed under MIT/X11. Thanks to [Sindhu](http://sindhus.bitbucket.org/) for the idea for this plugin.