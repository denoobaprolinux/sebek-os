import gi
import subprocess
import os

gi.require_version("Gtk", "4.0")
from gi.repository import Gtk, Gio

class HyprlandSettings(Gtk.Application):
    def __init__(self):
        super().__init__(application_id="sebekdots.settings")
        self.config = {
            "Anchura de Bordes de Ventanas": "numeric",
            "Gaps Internos": "numeric",
            "Gaps Externos": "numeric",
            "Smart Gaps": ["Encendido", "Apagado"],
            "Efecto Blur": ["Encendido", "Apagado"],
            "Efecto Neón": ["Encendido", "Apagado"],
            "Efecto Neón - Rango": "numeric",
            "Efecto Neón - Intensidad": "numeric",
            "Redimensionar Ventanas": ["Encendido", "Apagado"],
            "Redimensionar Ventanas - Área": "numeric",
            "Esquinas": "numeric",
            "Animaciones": [
                "Apagadas",
                "Estándar",
                "Desvanecer",
                "Rápidas",
                "Fluidas",
                "Máximas",
            ],
            "Oscurecimiento": ["Encendido", "Apagado"],
            "Oscurecimiento - Intensidad": "numeric",
            "Opacidad (Ventana Activa)": "numeric",
            "Opacidad (Ventana Inactiva)": "numeric",
            "Efecto Rayos X": ["Encendido", "Apagado"],
        }
        self.hyprctl_script = os.path.expanduser("~/.config/hypr/hyprctl.sh")
        if not os.path.isfile(self.hyprctl_script):
            with open(self.hyprctl_script, "w") as file:
                file.write("#!/bin/bash\n")
            os.chmod(self.hyprctl_script, 0o755)

    def update_hyprctl_script(self, key, value):
        pattern = f"^hyprctl keyword {key}"
        with open(self.hyprctl_script, "r") as file:
            lines = file.readlines()

        updated = False
        with open(self.hyprctl_script, "w") as file:
            for line in lines:
                if line.startswith(pattern):
                    if not line.strip().endswith(value):
                        line = f"hyprctl keyword {key} {value}\n"
                        updated = True
                file.write(line)
            if not updated:
                file.write(f"hyprctl keyword {key} {value}\n")

    def apply_setting(self, key, value):
        command = f"hyprctl keyword {key} {value}"
        subprocess.run(command, shell=True, check=True)

    def handle_option(self, selected_option, selected_value):
        if selected_option == "Configuración por defecto":
            if selected_value == "Aceptar":
                # Ejecutar recarga y restauración de configuración por defecto
                subprocess.run("hyprctl reload", shell=True, check=True)
                with open(self.hyprctl_script, "w") as file:
                    file.write("#!/bin/bash\n")
                os.chmod(self.hyprctl_script, 0o755)
                subprocess.run("cp ~/.config/hypr/config/animations/animations-default.conf ~/.config/hypr/config/animations.conf", shell=True)

        elif selected_option == "Anchura de Bordes de Ventanas":
            self.apply_setting("general:border_size", selected_value)
            self.update_hyprctl_script("general:border_size", selected_value)
        elif selected_option == "Gaps Internos":
            self.apply_setting("general:gaps_in", selected_value)
            self.update_hyprctl_script("general:gaps_in", selected_value)
        elif selected_option == "Gaps Externos":
            self.apply_setting("general:gaps_out", selected_value)
            self.update_hyprctl_script("general:gaps_out", selected_value)
        elif selected_option == "Smart Gaps":
            if selected_value == "Encendido":
                subprocess.run(f"cp ~/.config/hypr/config/gaps/gaps_on.conf ~/.config/hypr/config/gaps.conf", shell=True)
                subprocess.run("hyprctl reload", shell=True, check=True)
            elif selected_value == "Apagado":
                subprocess.run(f"cp ~/.config/hypr/config/gaps/gaps_off.conf ~/.config/hypr/config/gaps.conf", shell=True)
                subprocess.run("hyprctl reload", shell=True, check=True)
        elif selected_option == "Efecto Blur":
            if selected_value == "Encendido":
                self.apply_setting("decoration:blur:enabled", "true")
                self.update_hyprctl_script("decoration:blur:enabled", "true")
            elif selected_value == "Apagado":
                self.apply_setting("decoration:blur:enabled", "false")
                self.update_hyprctl_script("decoration:blur:enabled", "false")
        elif selected_option == "Efecto Neón":
            if selected_value == "Encendido":
                self.apply_setting("decoration:shadow:enabled", "true")
                self.update_hyprctl_script("decoration:shadow:enabled", "true")
            elif selected_value == "Apagado":
                self.apply_setting("decoration:shadow:enabled", "false")
                self.update_hyprctl_script("decoration:shadow:enabled", "false")
        elif selected_option == "Efecto Neón - Rango":
            self.apply_setting("decoration:shadow:range", selected_value)
            self.update_hyprctl_script("decoration:shadow:range", selected_value)
        elif selected_option == "Efecto Neón - Intensidad":
            self.apply_setting("decoration:shadow:render_power", selected_value)
            self.update_hyprctl_script("decoration:shadow:render_power", selected_value)
        elif selected_option == "Redimensionar Ventanas":
            if selected_value == "Encendido":
                self.apply_setting("general:resize_on_border", "true")
                self.update_hyprctl_script("general:resize_on_border", "true")
            elif selected_value == "Apagado":
                self.apply_setting("general:resize_on_border", "false")
                self.update_hyprctl_script("general:resize_on_border", "false")
        elif selected_option == "Redimensionar Ventanas - Área":
            self.apply_setting("general:extend_border_grab_area", selected_value)
            self.update_hyprctl_script("general:extend_border_grab_area", selected_value)
        elif selected_option == "Esquinas":
            self.apply_setting("decoration:rounding", selected_value)
            self.update_hyprctl_script("decoration:rounding", selected_value)
        elif selected_option == "Animaciones":
            animation_files = {
                "Apagadas": "animations-disabled.conf",
                "Estándar": "animations-default.conf",
                "Desvanecer": "animations-fade.conf",
                "Rápidas": "animations-fast.conf",
                "Fluidas": "animations-fluid.conf",
                "Máximas": "animations-maximum.conf",
            }
            selected_file = animation_files.get(selected_value)
            if selected_file:
                subprocess.run(f"cp ~/.config/hypr/config/animations/{selected_file} ~/.config/hypr/config/animations.conf", shell=True)
                subprocess.run("hyprctl reload", shell=True, check=True)
                self.apply_setting("animations:enabled", "true")
                self.update_hyprctl_script("animations:enabled", "true")
            else:
                self.apply_setting("animations:enabled", "false")
                self.update_hyprctl_script("animations:enabled", "false")
        elif selected_option == "Oscurecimiento":
            if selected_value == "Encendido":
                self.apply_setting("decoration:dim_inactive", "true")
                self.update_hyprctl_script("decoration:dim_inactive", "true")
            elif selected_value == "Apagado":
                self.apply_setting("decoration:dim_inactive", "false")
                self.update_hyprctl_script("decoration:dim_inactive", "false")
        elif selected_option == "Oscurecimiento - Intensidad":
            self.apply_setting("decoration:dim_strength", selected_value)
            self.update_hyprctl_script("decoration:dim_strength", selected_value)
        elif selected_option == "Opacidad (Ventana Activa)":
            self.apply_setting("decoration:opacity", selected_value)
            self.update_hyprctl_script("decoration:opacity", selected_value)
        elif selected_option == "Opacidad (Ventana Inactiva)":
            self.apply_setting("decoration:inactive_opacity", selected_value)
            self.update_hyprctl_script("decoration:inactive_opacity", selected_value)
        elif selected_option == "Efecto Rayos X":
            if selected_value == "Encendido":
                self.apply_setting("decoration:xray", "true")
                self.update_hyprctl_script("decoration:xray", "true")
            elif selected_value == "Apagado":
                self.apply_setting("decoration:xray", "false")
                self.update_hyprctl_script("decoration:xray", "false")

    def on_option_changed(self, combo, option):
        value = combo.get_active_text()
        self.handle_option(option, value)

    def on_numeric_changed(self, entry, option):
        value = entry.get_text()
        self.handle_option(option, value)

    def on_default_config(self, widget):
        # Acción para restaurar configuración por defecto
        self.handle_option("Configuración por defecto", "Aceptar")

    def do_activate(self):
        window = Gtk.ApplicationWindow(application=self)
        window.set_title("Configuración de Hyprland")
        window.set_default_size(400, 400)
        
        grid = Gtk.Grid(row_homogeneous=True, column_homogeneous=True)
        window.set_child(grid)

        # Botón de configuración por defecto
        default_button = Gtk.Button(label="Restaurar Configuración por Defecto")
        default_button.connect("clicked", self.on_default_config)
        grid.attach(default_button, 0, 0, 2, 1)

        i = 1
        for option, values in self.config.items():
            label = Gtk.Label(label=option)
            grid.attach(label, 0, i, 1, 1)

            if isinstance(values, list):
                combo = Gtk.ComboBoxText()
                for value in values:
                    combo.append_text(value)  # Aquí usamos append_text en lugar de append
                combo.set_active(0)
                combo.connect("changed", self.on_option_changed, option)
                grid.attach(combo, 1, i, 1, 1)
            elif values == "numeric":
                entry = Gtk.Entry()
                entry.set_text("0")
                entry.connect("changed", self.on_numeric_changed, option)
                grid.attach(entry, 1, i, 1, 1)

            i += 1

        window.present()

if __name__ == "__main__":
    app = HyprlandSettings()
    app.run()