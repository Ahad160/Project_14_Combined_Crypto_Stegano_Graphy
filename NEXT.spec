# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['DARK_main.py','Encryption_Folder.py','Image_Steganography.py','Google_Drive_API.py','Credentials_Key.json'],
    pathex=['E:\Codeing\Python Language\Projects\Project_14_DARK_Crypto_Stegano_Graphy'],
    binaries=[],
    datas=[('Credentials_Key.json', '.')],
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
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='NEXT',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
