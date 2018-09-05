# -*- mode: python -*-

block_cipher = None


a = Analysis(['run.py'],
             pathex=['/Users/numino/Desktop/santan-pixm/new-update'],
             binaries=[('/System/Library/Frameworks/Tk.framework/Tk','tk'),
                ('/System/Library/Frameworks/Tcl.framework/Versions/8.5/Tcl','tcl')],
             datas=[],
             hiddenimports=["Tkinter"],
             hookspath=['pyinstaller-hooks'],
             runtime_hooks=['pyinstaller-hooks/pyi_rth__tkinter.py'],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='run',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False )
app = BUNDLE(exe,
            a.binaries,
            a.zipfiles,
            a.datas,
            name='run.app',
            icon=None,
            bundle_identifier=None)
