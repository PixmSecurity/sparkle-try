import sys
from Tkinter import Tk
from tk import Application
from objc import pathForFramework, loadBundle
import tkMessageBox

root = Tk()
app = Application(master=root)

# URL to Appcast.xml, eg. https://yourserver.com/Appcast.xml
APPCAST_URL = 'https://enterprisemsidev.blob.core.windows.net/tempcont/updatecast.xml'
# Path to Sparkle's "Sparkle.framework" inside your app bundle
SPARKLE_PATH = '/Users/numino/Downloads/Sparkle-1.20.0/Sparkle.framework'
sparkle_path = pathForFramework(SPARKLE_PATH)
objc_namespace = dict()
loadBundle('Sparkle', objc_namespace, bundle_path=sparkle_path)

def ask_quit():
    if tkMessageBox.askokcancel("Quit", "You want to quit now?"):
        objc_namespace['NSApplication'].sharedApplication().terminate_(None)
        root.destroy()

root.protocol("WM_DELETE_WINDOW", ask_quit)
app.mainloop()
sparkle = objc_namespace['SUUpdater'].sharedUpdater()
sparkle.setAutomaticallyChecksForUpdates_(True)
sparkle.setAutomaticallyDownloadsUpdates_(True)
NSURL = objc_namespace['NSURL']
sparkle.setFeedURL_(NSURL.URLWithString_(APPCAST_URL))
sparkle.checkForUpdatesInBackground()
print "Check for updates in background"







