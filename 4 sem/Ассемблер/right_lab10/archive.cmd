@echo off
rem архивирует все исходники, пропускает все что компилировалось
rem !!! скрипт написан для русской локализации

rem локальный режим переменных
setlocal 
set path="C:\Program files\WinRAR"


rem формирование таймштампа
FOR /f "tokens=1-7 delims=/-:., " %%a IN ("%DATE: =0% %TIME: =0%") do (
    SET TIMESTAMP=_%%c%%b%%a_%%d%%e
)

rem формирование имени архива из имени папки, даты и времени
rem !!! цикл нужен для хитрости. к переменной %CD% нельзя применять ~ni, а вот к параметру цикла его применять можно.
rem в свою очередь %CD% может быть элементом списка файлов
for /d %%i in ("%CD%") do (
	set ARC_NAME=%%~ni%TIMESTAMP%.rar
	rem так можно для универсальной локализации
	rem set ARC_NAME=%%~ni_%date%_%time:~0,2%%time:~3,2%.rar
)

rem проверить, есть ли такой вайл
if not exist "%ARC_NAME%" (

rem  создать архив, главное здесь исключить ненужное
rem !!! запускаемое приложение отдельно в кавычках путь и отдельно имя файла
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
rem файл уже есть, нельзя пеерезаписывать
	echo file %ARC_NAME% is exist
)

endlocal
