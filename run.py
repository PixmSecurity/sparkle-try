import sys
from Tkinter import Tk
from tk import Application
from objc import pathForFramework, loadBundle
import tkMessageBox

# URL to Appcast.xml, eg. https://yourserver.com/Appcast.xml
APPCAST_URL = 'https://enterprisemsidev.blob.core.windows.net/tempcont/updatecast.xml'
# Path to Sparkle's "Sparkle.framework" inside your app bundle
SPARKLE_PATH = '/Library/Frameworks/Sparkle.framework'

root = Tk()
app = Application(APPCAST_URL, SPARKLE_PATH, master=root)
root.protocol("WM_DELETE_WINDOW", app.ask_quit)
root.lift()
root.attributes('-topmost',True)
root.after_idle(root.attributes,'-topmost',False)
app.mainloop()
