from cx_Freeze import setup, Executable

setup(
    name="Utasszallitok",
    version="1.0",
    description="My Application",
    executables=[Executable("GUI.py")],
    options={
        "build_exe": {
            "include_files": ["szub.png","mig.jpg","concorde.png","dulpafedele.png","utasszallitok.txt"]
        }
    }
)
