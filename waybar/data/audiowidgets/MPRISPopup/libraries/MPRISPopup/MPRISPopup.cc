#include "MPRISPopup.hpp"
#include <fstream>
#include <iostream>

MPRISPopup::MPRISPopup()
    : player{nullptr}, bg_color("#282828"), fg_color("#ebdbb2"),
      accent_color("#cc241d") {
  set_default_size(300, 250);
  set_resizable(false);
  set_decorated(false);
  set_modal(true);

  // Cargar colores de Pywal
  load_pywal_colors();

  // Aplicar estilo
  set_style();

  // Layout principal
  auto vbox = Gtk::Box(Gtk::Orientation::VERTICAL, 10);
  vbox.set_margin_start(10);
  vbox.set_margin_end(10);
  vbox.set_margin_top(10);
  vbox.set_margin_bottom(10);
  vbox.set_halign(Gtk::Align::CENTER);
  vbox.set_valign(Gtk::Align::CENTER);
  set_child(vbox);

  // Etiqueta del título
  label_title.set_wrap();
  label_title.set_wrap_mode(Pango::WrapMode::WORD_CHAR);
  label_title.set_max_width_chars(30);
  label_title.set_lines(3);
  label_title.set_ellipsize(Pango::EllipsizeMode::END);
  label_title.set_markup("<b>Título: Cargando...</b>");
  label_title.set_justify(Gtk::Justification::CENTER); // Centrar el texto
  label_title.set_halign(Gtk::Align::CENTER);          // Centrar el widget

  label_artist.set_markup("Artista: Desconocido");
  label_album.set_markup("Álbum: Desconocido");

  for (auto *label : {&label_title, &label_artist, &label_album}) {
    label->set_halign(Gtk::Align::CENTER);
    vbox.append(*label);
  }

  // Botones de control multimedia
  auto hbox = Gtk::Box(Gtk::Orientation::HORIZONTAL, 10);
  hbox.set_halign(Gtk::Align::CENTER);
  vbox.append(hbox);

  auto btn_prev = Gtk::Button("⏮");
  btn_prev.signal_clicked().connect(
      sigc::mem_fun(*this, &MPRISPopup::on_previous));
  hbox.append(btn_prev);

  auto btn_play_pause = Gtk::Button("⏯");
  btn_play_pause.signal_clicked().connect(
      sigc::mem_fun(*this, &MPRISPopup::on_play_pause));
  hbox.append(btn_play_pause);

  auto btn_next = Gtk::Button("⏭");
  btn_next.signal_clicked().connect(sigc::mem_fun(*this, &MPRISPopup::on_next));
  hbox.append(btn_next);

  // Control deslizante para el volumen
  scale_volume.set_range(0, 100);       // Establece el rango de 0 a 100
  scale_volume.set_value(get_volume()); // Configura el valor inicial usando
                                        // la función que obtiene el volumen
  scale_volume.set_digits(
      0); // Establece el número de dígitos después del punto decimal a 0
  scale_volume.set_halign(
      Gtk::Align::CENTER); // Centra el control deslizante en la ventana
  scale_volume.set_size_request(
      250, 20); // Asegura que el control deslizante sea más grande
  scale_volume.signal_value_changed().connect(sigc::mem_fun(
      *this,
      &MPRISPopup::on_volume_changed)); // Conecta la señal de cambio a la
                                        // función que ajusta el volumen
  vbox.append(scale_volume);

  // Inicializar Playerctl
  init_playerctl();
}

MPRISPopup::~MPRISPopup() {
  if (player)
    g_object_unref(player);
}

//------------------------------------------------------------------------------------------------------------------------------------
void MPRISPopup::load_pywal_colors() {
  // En esta funcion estaremos leyendo los colores definidos por paywal en la
  // ruta establecida.

  //! Levantar una exepcion para manejar posibles errores al abrir el archivo
  std::ifstream file(wal_colors_path);
  if (!file.is_open()) {
    std::cerr << "No se pudo abrir el archivo de colores de Pywal, usando "
                 "colores predeterminados."
              << std::endl;
    return;
  }

  int line_number = 0;
  while (std::getline(file, line)) {
    line_number++;

    switch (line_number) {
    case 1:
      bg_color = line;
    case 2:
      fg_color = line;
    case 3:
      accent_color = line;
    default:
      break;
    }

    // if (line_number == 1)
    //   bg_color = line;
    // else if (line_number == 2)
    //   fg_color = line;
    // else if (line_number == 3)
    //   accent_color = line;
    // if (line_number > 3)
    //   break;
  }
}

void MPRISPopup::set_style() {
  auto css = Glib::ustring::compose(R"(
      window {
          background-color: %1;
          color: %2;
          border-radius: 10px;
          border: 2px solid %3;
      }
      label {
          color: %3;
      }
      button {
          color: %2;
          background-color: %3;
          border-radius: 5px;
      }
      button:hover {
          background-color: %1;
          color: %1;
      }
  )",
                                    bg_color, fg_color, accent_color);

  auto style_provider = Gtk::CssProvider::create();
  style_provider->load_from_data(css);
  Gtk::StyleContext::add_provider_for_display(
      Gdk::Display::get_default(), style_provider,
      GTK_STYLE_PROVIDER_PRIORITY_APPLICATION);
}

void MPRISPopup::init_playerctl() {
  GError *error = nullptr;

  player = playerctl_player_new(nullptr, &error);
  if (!player) {
    std::cerr << "Error inicializando Playerctl: " << error->message
              << std::endl;
    g_error_free(error);
    return;
  }

  g_signal_connect(player, "metadata", G_CALLBACK(on_metadata_changed), this);
  update_info();
}

void MPRISPopup::update_info() {
  if (!player)
    return;
  GError *error = nullptr;

  gchar *title = playerctl_player_get_title(player, &error);
  gchar *artist = playerctl_player_get_artist(player, &error);
  gchar *album = playerctl_player_get_album(player, &error);

  label_title.set_markup(std::string("<b>") + (title ? title : "Desconocido") +
                         "</b>");
  label_artist.set_markup("Artista: " +
                          std::string(artist ? artist : "Desconocido"));
  label_album.set_markup("Álbum: " +
                         std::string(album ? album : "Desconocido"));

  g_free(title);
  g_free(artist);
  g_free(album);
}

void MPRISPopup::on_volume_changed() {
  int volume = static_cast<int>(scale_volume.get_value());
  std::string cmd =
      "pactl set-sink-volume @DEFAULT_SINK@ " + std::to_string(volume) + "%";
  std::system(cmd.c_str());
}

void MPRISPopup::on_previous() {
  if (player)
    playerctl_player_previous(player, nullptr);
}

void MPRISPopup::on_play_pause() {
  if (player)
    playerctl_player_play_pause(player, nullptr);
}

void MPRISPopup::on_next() {
  if (player)
    playerctl_player_next(player, nullptr);
}

int MPRISPopup::get_volume() {
  try {
    std::string cmd =
        "pactl get-sink-volume @DEFAULT_SINK@ | awk '{print $5}' | tr -d '%'";
    std::array<char, 128> buffer;
    std::string result;
    std::unique_ptr<FILE, decltype(&pclose)> pipe(popen(cmd.c_str(), "r"),
                                                  pclose);
    if (pipe) {
      while (fgets(buffer.data(), buffer.size(), pipe.get())) {
        result += buffer.data();
      }
    }
    return std::stoi(result);
  } catch (...) {
    return 50; // Si hay un error, establece el volumen a un valor
               // predeterminado (ej. 50)
  }
}

void MPRISPopup::on_metadata_changed(PlayerctlPlayer *player, GParamSpec *,
                                     gpointer user_data) {
  auto *self = static_cast<MPRISPopup *>(user_data);
  self->update_info();
}
