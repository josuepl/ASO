#!/bin/bash
echo "Ingresa un número:"
read num

if [ $num -gt 10 ]; then
    echo "$num es mayor que 10"
elif [ $num -eq 10 ]; then
    echo "$num es igual a 10"
else
    echo "$num es menor que 10"
fi