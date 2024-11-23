#!/bin/bash

# Definir el archivo de bloqueo y el ejecutable
LOCK_FILE="/tmp/mpris_widget.lock"
EXECUTABLE="$HOME/.config/waybar/data/audiowidgets/arriba/mpris-up"

# Función para obtener el PID de la instancia en ejecución
get_pid() {
    pgrep -f "$EXECUTABLE"
}

# Si ya hay una instancia en ejecución (es decir, el archivo de bloqueo está presente)
if [ -f "$LOCK_FILE" ]; then
    # Obtener el PID desde el archivo de bloqueo
    PID=$(cat "$LOCK_FILE")

    # Comprobar si el proceso sigue corriendo
    if ps -p $PID > /dev/null; then
        # Matar la instancia si está en ejecución
        kill $PID
        rm -f "$LOCK_FILE"  # Eliminar el archivo de bloqueo
    else
        # Si el proceso no está en ejecución, eliminar el archivo de bloqueo huérfano
        rm -f "$LOCK_FILE"
    fi
else
    # Si no hay ninguna instancia en ejecución, ejecutarla
    $EXECUTABLE &
    echo $! > "$LOCK_FILE"  # Guardar el PID de la nueva instancia
fi
