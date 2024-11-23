#!/usr/bin/env python3
import gi
import json
import os
import subprocess

gi.require_version('Playerctl', '2.0')  # Playerctl 2.0
gi.require_version('Gtk', '4.0')       # GTK 4
from gi.repository import Gtk, Playerctl, Gdk, Pango

class MPRISPopup(Gtk.Window):
    def __init__(self, application):
        super().__init__(title="Now Playing", application=application)
        self.set_default_size(300, 250)
        self.set_resizable(False)
        self.set_decorated(False)
        self.set_modal(True)

        # Cargar paleta de Pywal
        self.colors = self.load_pywal_colors()

        # Aplicar colores
        self.set_style()

        # Layout principal
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        vbox.set_margin_start(10)
        vbox.set_margin_end(10)
        vbox.set_margin_top(10)
        vbox.set_margin_bottom(10)
        vbox.set_halign(Gtk.Align.CENTER)
        vbox.set_valign(Gtk.Align.CENTER)
        self.set_child(vbox)

        # Información de la canción
        self.label_title = Gtk.Label()
        self.label_artist = Gtk.Label()
        self.label_album = Gtk.Label()

        self.label_title.set_wrap(True)
        self.label_title.set_wrap_mode(Pango.WrapMode.WORD_CHAR)
        self.label_title.set_max_width_chars(30)
        self.label_title.set_ellipsize(Pango.EllipsizeMode.NONE)

        self.label_title.set_markup("<b>Título: Cargando...</b>")
        self.label_artist.set_markup("Artista: Desconocido")
        self.label_album.set_markup("Álbum: Desconocido")

        for label in (self.label_title, self.label_artist, self.label_album):
            label.set_halign(Gtk.Align.CENTER)

        vbox.append(self.label_title)
        vbox.append(self.label_artist)
        vbox.append(self.label_album)

        # Botones de control multimedia
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        hbox.set_halign(Gtk.Align.CENTER)
        vbox.append(hbox)

        btn_prev = Gtk.Button(label="⏮")
        btn_prev.connect("clicked", self.on_previous)
        hbox.append(btn_prev)

        btn_play_pause = Gtk.Button(label="⏯")
        btn_play_pause.connect("clicked", self.on_play_pause)
        hbox.append(btn_play_pause)

        btn_next = Gtk.Button(label="⏭")
        btn_next.connect("clicked", self.on_next)
        hbox.append(btn_next)

        # Control deslizante para el volumen
        self.scale_volume = Gtk.Scale(orientation=Gtk.Orientation.HORIZONTAL)
        self.scale_volume.set_range(0, 100)
        self.scale_volume.set_value(self.get_volume())  # Sincronizar con el volumen actual
        self.scale_volume.set_digits(0)
        self.scale_volume.set_size_request(200, 30)
        self.scale_volume.set_halign(Gtk.Align.CENTER)
        self.scale_volume.connect("value-changed", self.on_volume_changed)
        vbox.append(self.scale_volume)

        # Inicializamos el reproductor
        self.player = Playerctl.Player()
        self.player.connect('metadata', self.on_metadata_changed)

        self.update_info()

    def load_pywal_colors(self):
        try:
            wal_colors_path = os.path.expanduser("~/.cache/wal/colors.json")
            with open(wal_colors_path, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            print("No se encontró el archivo de colores de Pywal. Usando colores por defecto.")
            return {
                "special": {"background": "#282828", "foreground": "#ebdbb2"},
                "colors": {"color1": "#cc241d"}
            }

    def set_style(self):
        css = f"""
        window {{
            background-color: {self.colors['special']['background']};
            color: {self.colors['special']['foreground']};
            border-radius: 10px;
            border: 2px solid {self.colors['colors']['color1']};
        }}
        label {{
            color: {self.colors['special']['foreground']};
        }}
        button {{
            color: {self.colors['special']['foreground']};
            background-color: {self.colors['colors']['color1']};
            border-radius: 5px;
        }}
        button:hover {{
            background-color: {self.colors['colors']['color1']};
            color: {self.colors['special']['background']};
        }}
        """
        style_provider = Gtk.CssProvider()
        style_provider.load_from_data(css.encode("utf-8"))
        Gtk.StyleContext.add_provider_for_display(
            Gdk.Display.get_default(),
            style_provider,
            Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
        )

    def update_info(self):
        try:
            title = self.player.get_title() or "Desconocido"
            artist = self.player.get_artist() or "Desconocido"
            album = self.player.get_album() or "Desconocido"

            self.label_title.set_markup(f"<b>{title}</b>")
            self.label_artist.set_markup(f"Artista: {artist}")
            self.label_album.set_markup(f"Álbum: {album}")
        except Exception as e:
            print(f"Error actualizando la información: {e}")
            self.label_title.set_markup("<b>Título: No disponible</b>")
            self.label_artist.set_markup("Artista: Desconocido")
            self.label_album.set_markup("Álbum: Desconocido")

    def get_volume(self):
        try:
            result = subprocess.run(
                ["pactl", "get-sink-volume", "@DEFAULT_SINK@"],
                capture_output=True,
                text=True
            )
            if result.returncode == 0:
                volume_line = result.stdout.strip()
                # Extraer el porcentaje de volumen (primer valor)
                return int(volume_line.split()[4].replace("%", ""))
        except Exception as e:
            print(f"Error obteniendo el volumen: {e}")
        return 50

    def on_volume_changed(self, scale):
        try:
            volume = int(scale.get_value())
            subprocess.run(["pactl", "set-sink-volume", "@DEFAULT_SINK@", f"{volume}%"])
        except Exception as e:
            print(f"Error ajustando el volumen: {e}")

    def on_metadata_changed(self, player, metadata):
        self.update_info()

    def on_previous(self, button):
        try:
            self.player.previous()
        except Exception as e:
            print(f"Error en el botón 'Anterior': {e}")

    def on_play_pause(self, button):
        try:
            self.player.play_pause()
        except Exception as e:
            print(f"Error en el botón 'Reproducir/Pausar': {e}")

    def on_next(self, button):
        try:
            self.player.next()
        except Exception as e:
            print(f"Error en el botón 'Siguiente': {e}")

class MPRISApplication(Gtk.Application):
    def __init__(self):
        super().__init__(application_id="sebekos.mpris.down")
    
    def do_activate(self):
        win = MPRISPopup(self)
        win.present()

if __name__ == "__main__":
    app = MPRISApplication()
    app.run()
