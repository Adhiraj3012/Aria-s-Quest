# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['forest_guardian_advanced.py'],
    pathex=[],
    binaries=[],
    datas=[('C:\\Users\\Adhir\\Desktop\\Python\\aria.png', '.'), ('C:\\Users\\Adhir\\Desktop\\Python\\trashtitan.png', '.'), ('C:\\Users\\Adhir\\Desktop\\Python\\oilbeast.png', '.'), ('C:\\Users\\Adhir\\Desktop\\Python\\smogzilla.png', '.'), ('C:\\Users\\Adhir\\Desktop\\Python\\level1bg.png', '.'), ('C:\\Users\\Adhir\\Desktop\\Python\\lvl2bg.png', '.'), ('C:\\Users\\Adhir\\Desktop\\Python\\lvl3bg.png', '.'), ('C:\\Users\\Adhir\\Desktop\\Python\\trashcan.png', '.'), ('C:\\Users\\Adhir\\Desktop\\Python\\oilb.png', '.'), ('C:\\Users\\Adhir\\Desktop\\Python\\emission.png', '.'), ('C:\\Users\\Adhir\\Desktop\\Python\\zapf_international_bold.ttf', '.')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='forest_guardian_advanced',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
