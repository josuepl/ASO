#!/bin/bash
read -p "Ingresa tu nombre: " nombre

if [ "$nombre" = "Admin" ]; then
    echo "Bienvenido, Administrador."
else
    echo "Hola, $nombre."
fi