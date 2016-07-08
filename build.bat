:: Deployment Build for application.  Only for Windows.
call startup.bat
@RD /S /Q "build"
@RD /S /Q "dist"
::pyinstaller --noconsole --hidden-import=h5py.defs --hidden-import=h5py.utils --hidden-import=h5py.h5ac --hidden-import=h5py._proxy peui/app.py
::pyinstaller --debug --hidden-import=Tkinter --hidden-import=FileDialog  "debug.py" --specpath="build" --path="peui"
pyinstaller --debug "debug.py" --specpath="build" --path="peui" --name="pecgui"
:: Exit
