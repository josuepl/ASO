#!/bin/bash
read -p "Elige un color (rojo/verde/azul): " color

case "$color" in
    "rojo")   echo "Es un color cálido." ;;
    "verde")  echo "Es un color frío." ;;
    "azul")   echo "Es un color primario." ;;
    *)        echo "Color no reconocido." ;;
esac