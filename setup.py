from cx_Freeze import setup, Executable

base = None

executables = [Executable("czrevsrv.py", base=base)]

packages = ["idna", "fastapi", "uvicorn", "starlette"]
options = {
    'build_exe': {
        'packages':packages,
    },
}

setup(
    name = "cztoolsserver",
    options = options,
    version = "1.0",
    description = 'cztools server hack',
    executables = executables
)