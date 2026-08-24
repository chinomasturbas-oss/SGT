# SOLUCIÓN PARA ERROR DE WALLET DE ORACLE

## El Problema

```
java.sql.SQLException: ORA-17956: No se ha podido analizar la ubicación de cartera proporcionada
TNS-04605: Error de sintaxis no válida: Carácter o LITERAL inesperado "(" 
```

**Causa:** La ruta del proyecto contiene paréntesis: `SGT11 (2)` y Oracle no puede procesar correctamente caracteres especiales sin escaparlos.

---

## ✅ SOLUCIÓN 1: MOVER EL PROYECTO (RECOMENDADO)

Esta es la forma más confiable.

### Paso 1: Copiar el proyecto a una ruta sin caracteres especiales

```bash
# Copia la carpeta completa de:
C:\Users\josee\OneDrive\Desktop\SGT11 (2)\project\SGT12

# A:
C:\SGT12
```

**En Windows Explorer:**
1. Abre: `C:\Users\josee\OneDrive\Desktop`
2. Haz click derecho en `SGT11 (2)` → Copiar
3. Ve a `C:\` 
4. Click derecho → Pegar
5. Renombra la carpeta a `SGT12`

### Paso 2: Abrir el proyecto en IntelliJ desde la nueva ubicación

1. En IntelliJ: `File → Open`
2. Selecciona: `C:\SGT12`
3. Click OK
4. Espera a que IntelliJ reindexe (verás una barra de progreso)

### Paso 3: Recompilar

1. `Build → Clean Project`
2. `Build → Rebuild Project`
3. `Build → Build Artifacts → SGT:war → Build`

### Paso 4: Desplegar

Copia el WAR a Tomcat:
```
Copiar: C:\SGT12\target\SGT-1.0-SNAPSHOT.war
A:      C:\Users\josee\OneDrive\Desktop\apache-tomcat-10.1.57-windows-x64\apache-tomcat-10.1.57\webapps\SGT.war
```

Reinicia Tomcat.

---

## ✅ SOLUCIÓN 2: DEJAR EN UBICACIÓN ACTUAL (CON CÓDIGO MEJORADO)

Si prefieres mantener el proyecto en su ubicación actual, he mejorado el código de `ConexionDB.java` para manejar caracteres especiales.

Ya han sido aplicados estos cambios:
1. Escapar paréntesis en la ruta del wallet
2. Usar `oracle.net.wallet_location` con comillas

### Para aplicar esto:

1. En IntelliJ: `Build → Rebuild Project`
2. `Build → Build Artifacts → SGT:war → Build`
3. Copia el WAR a Tomcat
4. Reinicia Tomcat

Si aún falla, entonces **DEBES usar la Solución 1** (mover a ruta sin paréntesis).

---

## 🧪 Prueba

Después de desplegar:

1. Abre: `http://localhost:8080/SGT/index.jsp`
2. Intenta login con:
   - Usuario: `admin@utez.edu.mx` (o un usuario existente en la BD)
   - Contraseña: (la correcta)
   - Rol: selecciona uno

3. **Si login funciona sin errores de wallet → ¡Problema resuelto!** ✅

---

## 📋 Checklist

- [ ] Decidí si mover a `C:\SGT12` o mantener en ubicación actual
- [ ] Recompilé el proyecto
- [ ] Generé el WAR
- [ ] Copié el WAR a `webapps/`
- [ ] Reinicié Tomcat
- [ ] Probé login en navegador
- [ ] Verifiqué que NO hay error de wallet

---

## 💡 ¿Por qué ocurre esto?

Oracle JDBC driver intenta analizar la ruta del wallet como un archivo de configuración TNS. Cuando hay caracteres especiales (paréntesis, espacios) sin escapar, Oracle interpreta los paréntesis como sintaxis de su lenguaje de configuración y falla.

Soluciones:
- **Mejor:** Ruta sin caracteres especiales
- **También funciona:** Escapar caracteres en código (ya lo hicimos)

---

## 🆘 Si Aún Falla

Si después de esto sigue fallando, probablemente es porque:

1. El wallet no está en el classpath o `src/main/resources`
2. La configuración de Tomcat no está correcta
3. Oracle JDBC driver tiene problemas con tu versión de Java

En ese caso:
- Verifica que el wallet (`Wallet_I8PKKA6947YK49EI`) esté en: `C:\SGT12\src\main\resources\`
- Verifica que contenga: `tnsnames.ora` y `sqlnet.ora`
- Prueba con la Solución 1 (mover a ruta sin paréntesis)
