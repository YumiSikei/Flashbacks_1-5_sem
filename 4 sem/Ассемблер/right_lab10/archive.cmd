@echo off
rem ���������� ��� ���������, ���������� ��� ��� ���������������
rem !!! ������ ������� ��� ������� �����������

rem ��������� ����� ����������
setlocal 
set path="C:\Program files\WinRAR"


rem ������������ ����������
FOR /f "tokens=1-7 delims=/-:., " %%a IN ("%DATE: =0% %TIME: =0%") do (
    SET TIMESTAMP=_%%c%%b%%a_%%d%%e
)

rem ������������ ����� ������ �� ����� �����, ���� � �������
rem !!! ���� ����� ��� ��������. � ���������� %CD% ������ ��������� ~ni, � ��� � ��������� ����� ��� ��������� �����.
rem � ���� ������� %CD% ����� ���� ��������� ������ ������
for /d %%i in ("%CD%") do (
	set ARC_NAME=%%~ni%TIMESTAMP%.rar
	rem ��� ����� ��� ������������� �����������
	rem set ARC_NAME=%%~ni_%date%_%time:~0,2%%time:~3,2%.rar
)

rem ���������, ���� �� ����� ����
if not exist "%ARC_NAME%" (

rem  ������� �����, ������� ����� ��������� ��������
rem !!! ����������� ���������� �������� � �������� ���� � �������� ��� �����
	"Rar.exe" a -r -ed ^
		 -x*\Release* -x*\Release*\* -x*\Debug* -x*\Debug*\* -x*\_Release* -x*\_Release*\* ^
		-x*\_Debug* -x*\_Debug*\* -x*\ipch* -x*\ipch*\* -x*\.* -x*\!\*.* ^
		-x*\LOG\* -x*\Config\* -x*\Documents\* ^
		-x*.sdf -x*.ncb -x*.suo -x*.rar -x*.log -x*.exe ^
		"%ARC_NAME%" ^
	|| (
		del "%ARC_NAME%" 
		echo error. file %ARC_NAME% is NOT created
	)
) else (
rem ���� ��� ����, ������ ���������������
	echo file %ARC_NAME% is exist
)

endlocal
