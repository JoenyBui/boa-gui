:: Deployment Build for application.  Only for Windows.
call startup.bat
@RD /S /Q "build/x64/boagui"
@RD /S /Q "dist/x64/boagui"
::pyinstaller --noconsole --hidden-import=h5py.defs --hidden-import=h5py.utils --hidden-import=h5py.h5ac --hidden-import=h5py._proxy boaui/app.py
::pyinstaller --debug --hidden-import=Tkinter --hidden-import=FileDialog  "debug.py" --specpath="build" --path="boaui"
::pyinstaller --debug "app.py" --specpath="build" --path="boaui" --name="pecgui"
pyinstaller --debug "app.py" --hidden-import=scipy.special.__ufuncs_cxx --hidden-import=scipy.special.__ufuncs --hidden-import=scipy.special.__ellip_harm --hidden-import=scipy.special.basic --hidden-import=scipy.special.generate_ufuncs --hidden-import=scipy.special.lambertw --hidden-import=scipy.special.orthogonal --hidden-import=scipy.special.specfun --workpath="build/x64" --distpath="dist/x64" --specpath="build/x64" --path="boaui" --name="boaui"
:: Exit
