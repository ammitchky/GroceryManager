for /F %%i in ("%CD%") do @set VENV=%%~ni
IF not EXIST %VENV%.venv python -m venv %VENV%.venv
%VENV%.venv\Scripts\pip.exe install -r requirements.txt
%VENV%.venv\Scripts\activate.bat