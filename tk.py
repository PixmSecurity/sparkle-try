from Tkinter import *
from objc import pathForFramework, loadBundle
import tkMessageBox

class Application(Frame):
    def __init__(self, APPCAST_URL, SPARKLE_PATH, master=None):
        Frame.__init__(self, master)
        self.APPCAST_URL = APPCAST_URL
        self.SPARKLE_PATH = SPARKLE_PATH
        self.objc_namespace = dict()
        self.pack()
        self.createWidgets()
    
    def check_for_updates(self):
        sparkle_path = pathForFramework(self.SPARKLE_PATH)
        loadBundle('Sparkle', self.objc_namespace, bundle_path=sparkle_path)

        sparkle = self.objc_namespace['SUUpdater'].sharedUpdater()
        sparkle.setAutomaticallyChecksForUpdates_(True)
        sparkle.setAutomaticallyDownloadsUpdates_(True)
        NSURL = self.objc_namespace['NSURL']
        sparkle.setFeedURL_(NSURL.URLWithString_(self.APPCAST_URL))
        sparkle.checkForUpdatesInBackground()
        print "Check for updates in background"
    
    def ask_quit(self):
        if tkMessageBox.askokcancel("Quit", "You want to quit now?"):
            self.objc_namespace['NSApplication'].sharedApplication().terminate_(None)
            self.destroy()

    def createWidgets(self):
        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] =  self.quit

        self.QUIT.pack({"side": "left"})

        self.check_updates = Button(self)
        self.check_updates["text"] = "CheckForUpdates",
        self.check_updates["command"] = self.check_for_updates

        self.check_updates.pack({"side": "left"})

