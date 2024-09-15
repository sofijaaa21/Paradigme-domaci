@echo off
REM Skript za brisanje .bak, .log i .tmp datoteka u tekućem i svim poddirektorijumima

echo Uklanjanje pomoćnih datoteka (*.bak, *.log, *.tmp) u tekućem direktorijumu i poddirektorijumima...

REM Brisanje .bak, .log i .tmp datoteka
for /r %%i in (*.bak *.log *.tmp) do (
    echo Brisanje %%i
    del "%%i"
)

echo Brisanje završeno.
pause
