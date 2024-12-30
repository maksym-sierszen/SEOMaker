# -*- mode: python ; coding: utf-8 -*-
block_cipher = None

# Analysis step: Analyze the dependencies of the script
a = Analysis(
    ['SEOMaker.py'],  # Main Python script
    pathex=[],  # Additional paths to search for imports (if required)
    binaries=[('C:/hostedtoolcache/windows/Python/3.9.13/x64/python39.dll', '.')],  # Include python39.dll
    datas=[],  # Additional data files (e.g., images, text files)
    hiddenimports=[],  # Hidden imports that PyInstaller might not detect
    hookspath=[],  # Paths to custom PyInstaller hooks
    runtime_hooks=[],  # Hooks to execute during runtime
    excludes=[],  # Modules to exclude from the build
    win_no_prefer_redirects=False,  # Windows-specific configuration
    win_private_assemblies=False,  # Use private assemblies on Windows
    cipher=block_cipher,  # Optional encryption for bytecode
    noarchive=False,  # Prevent archiving; keeps files extracted
)

# Create a Python executable
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,  # The compiled Python code
    a.scripts,  # Entry-point scripts
    [],
    exclude_binaries=False,  # Include binaries in the executable
    name='SEOMaker.exe',  # Name of the resulting executable file
    debug=False,  # Disable debug mode
    bootloader_ignore_signals=False,  # Bootloader ignores termination signals
    strip=False,  # Do not strip debug symbols
    upx=True,  # Enable UPX compression (optional)
    console=False,  # Disable console window (use windowed mode)
    icon='resources/icon.ico',  # Path to the application icon
    onefile=True,  # Package everything into a single executable
)
