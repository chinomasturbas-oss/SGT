@echo off
setlocal enabledelayedexpansion

REM Obtener la ruta del script
set SCRIPT_PATH=%~dp0
cd /d "%SCRIPT_PATH%"

echo Ruta del proyecto: %cd%
echo.

REM Paso 1: Limpiar
echo [1/3] Limpiando compilaciones anteriores...
call mvnw.cmd clean -q 2>nul
if !ERRORLEVEL! NEQ 0 (
    echo Error en clean, intentando con rutas largas...
    call mvnw.cmd clean 2>&1 | findstr /V "^\[" > output.log
    type output.log | tail -20
)

REM Paso 2: Compilar
echo [2/3] Compilando...
call mvnw.cmd compile -q 2>nul
if !ERRORLEVEL! NEQ 0 (
    echo Error en compile, mostrando detalles:
    call mvnw.cmd compile 2>&1 | findstr /I "error"
    goto error
)

REM Paso 3: Package
echo [3/3] Empaquetando...
call mvnw.cmd package -DskipTests -q 2>nul
if !ERRORLEVEL! NEQ 0 (
    echo Error en package
    call mvnw.cmd package -DskipTests 2>&1 | findstr /I "error"
    goto error
)

echo.
echo ========================================
echo COMPILACION EXITOSA
echo ========================================
echo.
dir target\*.war
echo.
goto end

:error
echo.
echo ========================================
echo ERROR DURANTE LA COMPILACION
echo ========================================
echo.
pause
endlocal
exit /b 1

:end
endlocal
exit /b 0
