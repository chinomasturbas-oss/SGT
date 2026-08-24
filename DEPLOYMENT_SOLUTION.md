# SOLUCIÓN PARA ERROR DE DEPLOYMENT EN TOMCAT

## Problema
```
Configuration Error: deployment source 'SGT:war exploded' is not valid
Artifact SGT:war exploded: Error during artifact deployment
```

## Causa
El artifact "war exploded" no está correctamente configurado en IntelliJ IDEA

## SOLUCIÓN - SIGUE ESTOS PASOS EN INTELLIJ IDEA

### Paso 1: Limpiar Cache de IntelliJ
1. En IntelliJ IDEA: `File → Invalidate Caches → Invalidate and Restart`
2. Espera a que reinicie

### Paso 2: Reconstruir el Proyecto
1. `Build → Clean Project` (espera a que termine)
2. `Build → Rebuild Project` (espera a que compile todo)

### Paso 3: Configurar Tomcat Correctamente
1. Ir a: `Run → Edit Configurations`
2. Busca y selecciona tu configuración de Tomcat (probablemente "Tomcat 10.1.57")
3. En la pestaña "Deployment":
   - Si hay algún artifact listado, **elimínalo** (click en -)
   - Click en `+` para agregar artifact
   - Selecciona: `SGT:war` (NO "war exploded")
   - En "Application context" pon: `/`
4. Click en "Apply" y "OK"

### Paso 4: Ejecutar
1. `Run → Run 'Tomcat 10.1.57'` (o el nombre de tu config)
2. Deberías ver el mensaje de "Connected to server" sin errores

## SI AÚN FALLA - OPCIÓN NUCLEAR

### Método: Deployment Manual

1. En IntelliJ: `Build → Build Artifacts → SGT:war → Build`
2. El WAR se genera en: `target/SGT-1.0-SNAPSHOT.war`
3. Detén Tomcat
4. Copia el WAR a: 
   ```
   C:\Users\josee\OneDrive\Desktop\apache-tomcat-10.1.57-windows-x64\apache-tomcat-10.1.57\webapps\SGT.war
   ```
5. Inicia Tomcat
6. Tomcat extraerá automáticamente el WAR

## VERIFICACIÓN

Una vez deployado correctamente, verás en el Tomcat log:

```
INFO [main] org.apache.catalina.startup.Catalina.start Server startup in [XXX] milliseconds
Connected to server
```

SIN errores de "Configuration Error" o "deployment source"

## URLS DESPUÉS DEL DEPLOYMENT

- Principal: `http://localhost:8080/SGT`
- Login: `http://localhost:8080/SGT/index.jsp`
- API de prueba: `http://localhost:8080/SGT/api/usuarios/tutores`

---

Si después de estos pasos SIGUE fallando, es probable que sea un problema con tu instalación local de Tomcat o Maven. En ese caso reporta exactamente cuál es el nuevo error.
