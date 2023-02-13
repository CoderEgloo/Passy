from setuptools import setup

APP = ['passy.py']
DATA_FILES = ["icon.png"]
OPTIONS = {
    'iconfile':'icon.png',
    'argv_emulation': True,
    'plist': {
        'LSUIElement': True,
    },
    'packages': ['rumps', 'pyperclip', 'secrets', 'string'],
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)