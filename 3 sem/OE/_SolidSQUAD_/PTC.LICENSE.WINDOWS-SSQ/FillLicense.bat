@echo off

echo.
echo PTC Creo License Host ID Script
echo     2016 TeAM SolidSQUAD-SSQ
echo.

pushd "%~dp0"

del /Q /S "PTC_D_SSQ.dat"

for /F "tokens=4" %%b in ('ptc_hostid.exe ^| findstr "PTC HOSTID"') do set "PTCHOSTID=%%b"

for /f "tokens=* delims=" %%a in (PTC_D_SSQ.dat.template) do ( 
  setlocal EnableDelayedExpansion
  set "LINE=%%a" 
  set LINE=!LINE:00-00-00-00-00-00=%PTCHOSTID%!
  set LINE=!LINE!
  echo !LINE!>> "%~dp0PTC_D_SSQ.dat"
  endlocal
)

popd
pause
