# KivyCalculator
A simple calculator using Python and Kivy Lang.

For Standalone desktop application, follow the further steps.

--[Set A]-----------------
    1. Copy [.py] and [.kv] files.
    2. Create a new folder, i created as [DC_Calci].
    3. Paste both files inside the [DC_Calci] Folder

--[Set B]-----------------
    1. Open cmd-prompt as administrator.
    2. If you used Virtual environment, activate and then follow (i)(ii),
        (i). "pip install pyinstaller" [Net connection must only to download once] [Hit Enter]
        (ii). "pip freeze"/"pip list" [To check] [Hit enter

--[Set C]-----------------
    1. go to the newly created folder [DC_Calci] in cmd-prompt, by using cd 'PATH'
        For me : 'cd C:\Users\Pika pie\Desktop\KivyProjects\DC_Calci' [Hit Enter]
    2. Type "pyinstaller main_calci.py -w" [Hit Enter]
    3. Few files and folder will be automatically created by step 2. [dist] [.spec]
    4. Don't close the cmd-prompt

--[Set D]-----------------
    1. Open [main_calci.spec] in code editor.
    2. Make some changes in the [.spec] file.
        (i).   In top, write "from kivy_deps import sdl2, glew"
        (ii).  In between [pyz] and [exe] section, write the following,
                    "a.datas += [('Code\design.kv', 'C:\\Users\\Pika pie\\Desktop\\KivyProjects\\DC_Calci\design.kv', 'DATA')]"
                    (Hint): Every folder must have [\\] and file will have [\].
        (iii). In [Coll] section, add the below,
                    [Refer the set E for will edit]

--[Set E]-----------------
    1. Before Editing [.spec],

            # -*- mode: python ; coding: utf-8 -*-
            
            
            block_cipher = None
            
            
            a = Analysis(
                ['main_calci.py'],
                pathex=[],
                binaries=[],
                datas=[],
                hiddenimports=[],
                hookspath=[],
                hooksconfig={},
                runtime_hooks=[],
                excludes=[],
                win_no_prefer_redirects=False,
                win_private_assemblies=False,
                cipher=block_cipher,
                noarchive=False,
            )
            pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)
            
            exe = EXE(
                pyz,
                a.scripts,
                [],
                exclude_binaries=True,
                name='main_calci',
                debug=False,
                bootloader_ignore_signals=False,
                strip=False,
                upx=True,
                console=False,
                disable_windowed_traceback=False,
                argv_emulation=False,
                target_arch=None,
                codesign_identity=None,
                entitlements_file=None,
            )
            coll = COLLECT(
                exe,
                a.binaries,
                a.zipfiles,
                a.datas,
                strip=False,
                upx=True,
                upx_exclude=[],
                name='main_calci',
            )

    2. After Editing [.spec] file,

            # -*- mode: python ; coding: utf-8 -*-
            
            
            block_cipher = None
            
            
            a = Analysis(
                ['main_calci.py'],
                pathex=[],
                binaries=[],
                datas=[],
                hiddenimports=[],
                hookspath=[],
                hooksconfig={},
                runtime_hooks=[],
                excludes=[],
                win_no_prefer_redirects=False,
                win_private_assemblies=False,
                cipher=block_cipher,
                noarchive=False,
            )
            pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)
            
            exe = EXE(
                pyz,
                a.scripts,
                [],
                exclude_binaries=True,
                name='main_calci',
                debug=False,
                bootloader_ignore_signals=False,
                strip=False,
                upx=True,
                console=False,
                disable_windowed_traceback=False,
                argv_emulation=False,
                target_arch=None,
                codesign_identity=None,
                entitlements_file=None,
            )
            coll = COLLECT(
                exe,
                a.binaries,
                a.zipfiles,
                a.datas,
                strip=False,
                upx=True,
                upx_exclude=[],
                name='main_calci',
            )
   
    3. Save the file.

--[Set F]-----------------
    1. Go into the same cmd-prompt and type, "pyinstaller main_calci.spec -y"
    2. Go to file manager >> DC_Calci >> dist >> main_calci >> main_calci.exe
    3. Double click the file to get the standalone app.
