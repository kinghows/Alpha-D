from distutils.core import setup 
import py2exe 
includes = ["encodings", "encodings.*"] 
options = {"py2exe": 
{ "compressed": 1, 
"optimize": 2, 
"includes": includes, 
"bundle_files": 1 
} 
} 
setup( 
version = "1.0.0", 
description = "windows program", 
name = "jump", 
options = { "py2exe":{"dll_excludes":["MSVCP90.dll"]}},
zipfile=None, 
windows=[{"script": "Alpha-D.py", "icon_resources": [(1, "at.ico")]}], 
)
