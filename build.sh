#!/bin/bash
# Script simple para compilar en bash/gitbash

cd "$(dirname "$0")"

echo "Limpiando..."
./mvnw clean -q

echo "Compilando..."
./mvnw compile -q

echo "Empaquetando..."
./mvnw package -DskipTests -q

if [ -f target/SGT-1.0-SNAPSHOT.war ]; then
    echo "✅ WAR generado exitosamente"
    echo "   Ubicación: target/SGT-1.0-SNAPSHOT.war"
    ls -lh target/SGT-1.0-SNAPSHOT.war
else
    echo "❌ Error: WAR no fue generado"
    exit 1
fi
