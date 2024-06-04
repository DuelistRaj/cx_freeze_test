import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# Microsoft Visual C++ Redistributable for Visual Studio

base = None
if sys.platform == "win32":
    base = "Win32GUI"

build_exe_options = {
    "packages": ["streamlit", "PySide6", "pytz"],
    "include_files": ["test.py"],  # Include your main script file
}

setup(
    name="MyApp",
    version="1.0",
    description="My Application",
    options={"build_exe": build_exe_options},
    executables=[Executable("global.py", base=base)],
)