#!/bin/bash
read -p "Ingresa una contraseña: " pass

if [ -z "$pass" ]; then
    echo "Error: La contraseña no puede estar vacía."
else
    echo "Contraseña válida."
fi