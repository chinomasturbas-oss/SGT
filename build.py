#!/usr/bin/env python3
"""
Script para compilar y desplegar el proyecto SGT12
"""
import os
import sys
import subprocess
import shutil
from pathlib import Path

def run_command(cmd, cwd=None):
    """Ejecuta un comando y retorna el resultado"""
    try:
        result = subprocess.run(
            cmd,
            cwd=cwd,
            shell=True,
            capture_output=True,
            text=True,
            timeout=300
        )
        return result.returncode, result.stdout, result.stderr
    except subprocess.TimeoutExpired:
        return -1, "", "TIMEOUT"
    except Exception as e:
        return -1, "", str(e)

def main():
    project_root = Path(__file__).parent
    print(f"📁 Directorio del proyecto: {project_root}")
    print()
    
    # Paso 1: Clean
    print("🧹 [1/5] Limpiando...")
    code, out, err = run_command("mvnw.cmd clean -q", cwd=project_root)
    if code != 0:
        print(f"❌ Error en clean: {err}")
        return False
    print("✅ Clean completado")
    
    # Paso 2: Compile
    print("🔨 [2/5] Compilando...")
    code, out, err = run_command("mvnw.cmd compile -q", cwd=project_root)
    if code != 0:
        print(f"❌ Error en compile:")
        print(err)
        return False
    print("✅ Compilación completada")
    
    # Paso 3: Package
    print("📦 [3/5] Empaquetando...")
    code, out, err = run_command("mvnw.cmd package -DskipTests -q", cwd=project_root)
    if code != 0:
        print(f"❌ Error en package: {err}")
        return False
    print("✅ Package completado")
    
    # Paso 4: Verificar WAR
    war_file = project_root / "target" / "SGT-1.0-SNAPSHOT.war"
    if not war_file.exists():
        print(f"❌ WAR no encontrado: {war_file}")
        return False
    print(f"✅ WAR generado: {war_file.name}")
    
    # Paso 5: Copiar a Tomcat
    tomcat_path = Path("C:\\Users\\josee\\OneDrive\\Desktop\\apache-tomcat-10.1.57-windows-x64\\apache-tomcat-10.1.57\\webapps")
    if not tomcat_path.exists():
        print(f"⚠️  Tomcat no encontrado: {tomcat_path}")
        print("   Saltando deployment automático")
    else:
        print(f"🚀 [4/5] Desplegando en Tomcat...")
        
        # Eliminar deployment anterior
        old_war = tomcat_path / "SGT.war"
        old_dir = tomcat_path / "SGT"
        
        if old_dir.exists():
            shutil.rmtree(old_dir, ignore_errors=True)
        if old_war.exists():
            old_war.unlink()
        
        # Copiar nuevo WAR
        try:
            shutil.copy2(war_file, old_war)
            print(f"✅ WAR copiado a Tomcat")
        except Exception as e:
            print(f"❌ Error copiando WAR: {e}")
            return False
    
    print()
    print("=" * 50)
    print("✅ COMPILACIÓN Y DEPLOYMENT EXITOSOS")
    print("=" * 50)
    print()
    print(f"📍 URL de la aplicación: http://localhost:8080/SGT")
    print()
    
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
