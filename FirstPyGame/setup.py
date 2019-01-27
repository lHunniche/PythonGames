import cx_Freeze, os

os.environ['TCL_LIBRARY'] = r'C:\Users\Lasse\AppData\Local\Programs\Python\Python36\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Users\Lasse\AppData\Local\Programs\Python\Python36\tcl\tk8.6'

path = ""

executables = [cx_Freeze.Executable(path + "main.py", base = "Win32GUI", targetName="program.exe")]

cx_Freeze.setup(
    name="TypeMaster",
    options={"build_exe": {"packages":["pygame"],
                           "include_files": ["assets", "highscore.txt"]}},
    executables = executables
    )


#, cx_Freeze.Executable(path + "score.py"), cx_Freeze.Executable(path + "wordListProgramming.py"),
#               cx_Freeze.Executable(path + "wordListMIT.py"), cx_Freeze.Executable(path + "highscore.py"), cx_Freeze.Executable(path + "explosion.py"),
#              cx_Freeze.Executable(path + "backgroundmusic.py")


