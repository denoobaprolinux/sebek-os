#!/bin/bash

# Archivo temporal para gestionar el estado
LOCK_FILE="/tmp/mpris_widget.lock"

if [ -f "$LOCK_FILE" ]; then
    # Si el archivo existe, mata la ventana existente
    pkill -f "mpris-up.py"
    rm "$LOCK_FILE"
else
    # Si no existe, abre la ventana
    python3 ~/.config/waybar/data/audiowidgets/arriba/mpris-up.py &
    echo $$ > "$LOCK_FILE"
fi
