@echo off
setlocal
:begin
REM cls
echo [Menu] -------------------------------------------------------------
echo   1  -- cmd
echo   2  -- venv cmd
echo   3  -- Editor IDLE
echo   44 -- JupyterLab
echo   48 -- JupyterLab LAN
echo   4  -- Jupyter
echo   5  -- VISA info
echo   6  -- VISA shell
echo   7  -- Serial Terminal
echo   8  -- Code Standards
echo   9  -- Purge
echo;
echo   87 -- pip list
echo   88 -- Checkinstall
echo   89 -- Install
echo   90 -- Requirements
echo;
echo   x  -- exit
echo;
set /P rmFunc="Enter a choice: "
echo --------------------------------------------------------------------
for %%I in (1 2 3 4 44 48 5 6 7 8 9 88 89 90 x) do if #%rmFunc%==#%%I goto run%%I
goto begin

:breaker
REM If you provide no input to the menu it runs the next line regardless
REM This :breaker returns to the menu
goto begin

:install
echo install
python -m pip install --upgrade pip
python.exe -m venv venv
call venv\scripts\activate
python -m pip install --upgrade pip 
call :requirements
call venv\scripts\deactivate
goto :eof


:checkinstall
echo checkinstall
IF NOT EXIST "venv\" call :install
goto :eof



:requirements
call :checkinstall
echo requirements
call venv\scripts\activate
python -m pip install --upgrade -r requirements.txt
call venv\scripts\deactivate
goto :eof


:jupyterlab
call :checkinstall
call venv\scripts\activate
jupyter serverextension enable --py jupyterlab --sys-prefix
jupyter lab
call venv\scripts\deactivate
goto :eof

:jupyterlablan
call :checkinstall
call venv\scripts\activate
jupyter serverextension enable --py jupyterlab --sys-prefix
jupyter lab --ip=0.0.0.0 --port=80
call venv\scripts\deactivate
goto :eof


:jupyter
call :checkinstall
call venv\scripts\activate
jupyter nbextension enable --py widgetsnbextension --sys-prefix
jupyter notebook
call venv\scripts\deactivate
goto :eof


:serialterm
call :checkinstall
call venv\scripts\activate
python venv\scripts\miniterm.py
goto :eof

:visainfo
call :checkinstall
call venv\scripts\activate
python -m visa info > 00
type 00
pause
del 00
goto :eof

:visashell
call venv\scripts\activate
echo http://pyvisa.readthedocs.io/en/stable/shell.html
start python -m visa shell
goto :eof


:runmain
REM call 189-rewrite-venv-prefix
call venv\scripts\activate
start python main.py

REM pause
goto :eof

:codestandards
REM call 189-rewrite-venv
call venv\scripts\activate

python -m py.test --flakes --pep8 --ignore=venv --ignore=Legacy
REM --cov=prototype
pause
goto :eof


:editor
call venv\scripts\activate
start python -m idlelib
REM goto checkinstall
goto :eof


:run1
cmd
pause
goto begin

:run2
call venv\scripts\activate
cmd
goto begin

:run3
call :editor
goto begin

:run44
call :jupyterlab
goto begin

:run48
call :jupyterlablan
goto begin


:run4
call :jupyter
goto begin

:run5
call :visainfo
goto begin

:run6
call :visashell
goto begin

:run7
call :serialterm
goto begin

:run8
call :codestandards
goto begin

:run9
REM rmdir /s "venv/"
pause
goto begin


:run88
echo enter88
call :checkinstall
goto begin

:run89
call :install
goto begin

:run90
call :requirements
goto begin

rem and so on, until...

:runx
endlocal
goto :EOF