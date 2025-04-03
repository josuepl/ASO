#!/bin/bash
contador=1
while [ $contador -le 5 ]; do
    echo "Contador: $contador"
    ((contador++))
done