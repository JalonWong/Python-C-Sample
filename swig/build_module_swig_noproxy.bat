@ set PythonPath="C:\Program Files\Python35"
@ PATH=%PATH%;"C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC"

call swig -python -noproxy great_module.i 
call vcvarsall.bat amd64
cl /LD great_module_wrap.c /Fe"great_module.pyd" /I%PythonPath%\include %PythonPath%\libs\python35.lib
pause