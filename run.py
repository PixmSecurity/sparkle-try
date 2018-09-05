import sys
from Tkinter import Tk
from tk import Application
from objc import pathForFramework, loadBundle

root = Tk()
app = Application(master=root)
app.mainloop()
#root.destroy()

# URL to Appcast.xml, eg. https://yourserver.com/Appcast.xml
APPCAST_URL = 'https://enterprisemsidev.blob.core.windows.net/tempcont/updatecast.xml'
# Path to Sparkle's "Sparkle.framework" inside your app bundle
SPARKLE_PATH = '/Users/numino/Downloads/Sparkle-1.20.0/Sparkle.framework'
sparkle_path = pathForFramework(SPARKLE_PATH)
objc_namespace = dict()
loadBundle('Sparkle', objc_namespace, bundle_path=sparkle_path)

sparkle = objc_namespace['SUUpdater'].sharedUpdater()
sparkle.setAutomaticallyChecksForUpdates_(True)
sparkle.setAutomaticallyDownloadsUpdates_(True)
NSURL = objc_namespace['NSURL']
sparkle.setFeedURL_(NSURL.URLWithString_(APPCAST_URL))
sparkle.checkForUpdatesInBackground()

sys.exit(root.destroy())
