import os

cmd = """
osascript -e '
tell application "TextEdit"
	activate
end tell

tell application "System Events"
	keystroke "hello, World"
	key code 36
	keystroke "Goodbye"
end tell' 
"""


os.system(cmd)


