# CORRECCIÓN DEL ERROR DE NullPointerException EN AUTHSERVLET

## ✅ Lo que cambié

En `AuthServlet.java` línea 91, cambié:
```java
Logger.getLogger(AuthServlet.class.getName()).log(Level.SEVERE, null, e);
```

Por:
```java
Logger.getLogger(AuthServlet.class.getName()).log(Level.SEVERE, "Error al iniciar sesión", e);
```

**Causa del error:** El logger no puede manejar un mensaje `null` en Tomcat. Ahora tiene un mensaje descriptivo.

---

## 🔄 Pasos para aplicar la corrección

### Opción 1: Recompilar en IntelliJ (RECOMENDADO)

1. En IntelliJ IDEA, presiona: **Ctrl+F9** (Build Project)
   - O: `Build → Build Project`
   
2. Espera a que termine la compilación (verás "Build completed" abajo)

3. Luego: `Build → Build Artifacts → SGT:war → Build`
   - Espera a que se genere el WAR

4. **Copia** el nuevo WAR a Tomcat:
   ```
   Copiar: target\SGT-1.0-SNAPSHOT.war
   A:      C:\Users\josee\OneDrive\Desktop\apache-tomcat-10.1.57-windows-x64\apache-tomcat-10.1.57\webapps\SGT.war
   ```

5. **Reinicia Tomcat:**
   - En IntelliJ: `Run → Rerun 'Tomcat 10.1.57'`
   - O click en el botón de restart

### Opción 2: Línea de comandos (usando Git Bash / Terminal)

**En Git Bash o cualquier terminal que ejecute bash:**

```bash
cd "C:\Users\josee\OneDrive\Desktop\SGT11 (2)\project\SGT12"
./mvnw clean compile package -DskipTests -q
```

Luego copia el WAR generado a la carpeta `webapps` de Tomcat.

### Opción 3: Usando Maven directamente

```cmd
cd C:\Users\josee\OneDrive\Desktop\SGT11 (2)\project\SGT12
mvnw clean compile package -DskipTests
```

---

## ✅ Verificación

Después de recompilar y reiniciar Tomcat:

1. Abre en el navegador: `http://localhost:8080/SGT/index.jsp`
2. Intenta hacer login
3. **Si funciona sin errores**, ¡la corrección fue exitosa! ✅

Si ves el mismo error `NullPointerException`, algo no se recompilóco correctamente.

---

## 📋 Resumen

- El error venía de un logging incorrecto en AuthServlet
- Ya está corregido en el código
- Solo necesitas recompilar y desplegar nuevamente
- El error debería desaparecer completamente
