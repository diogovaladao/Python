import sys
from cx_Freeze import setup, Executable

build_exe_options = {"packages": ["openpyxl"], "includes": ["PIL"]}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="Assinatura",
    version="0.1",
    description="Gera assinaturas!",
    options={"build_exe": build_exe_options},
    executables=[Executable("assinatura.py", base=base)]
)