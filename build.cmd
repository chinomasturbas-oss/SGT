@echo off
REM Script para compilar el proyecto SGT12
cd /d "%~dp0"
echo Directorio actual: %cd%
echo.
echo Compilando proyecto...
call mvnw.cmd clean compile -q
if %ERRORLEVEL% EQU 0 (
    echo.
    echo Compilación exitosa
    echo Directorio target:
    dir target
) else (
    echo.
    echo Error en la compilación
    call mvnw.cmd clean compile
)
pause
